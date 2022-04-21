import json
import time

from protocol.MqttProtocol import MqttPublishProtocol
from utility.HexMessageFmtHelper import HexMessageFmt
from utility.DataCenterHelper import DataCenterHelper
from configure import settings


class UploadIOTStatus:
    def __init__(self, mqtt_helper, log_helper):
        self.log_helper = log_helper
        self.mqtt_helper = mqtt_helper
        self.datacenter_helper = DataCenterHelper()

        self.__pick_lane_status = {}
        self.init_pick_lane_status_group()

    async def init_pick_lane_status_group(self):
        # Q1: 如何知道PickLane为空
        # A1: 先获取初始数据：根据表划分出PickLane不同的iot列表，在就收IOT状态更新时，若改变，改变列表中的值后
        # 如
        # test1 = [
        #     {"PickLane": "PickLane1", "DeviceSerialNumber": "01020000"},
        #     {"PickLane": "PickLane1", "DeviceSerialNumber": "222"},
        #     {"PickLane": "PickLane1", "DeviceSerialNumber": "111111"},
        #     {"PickLane": "PickLane2", "DeviceSerialNumber": "01020000"},
        #     {"PickLane": "PickLane3", "DeviceSerialNumber": "333"},
        #     {"PickLane": "PickLane1", "DeviceSerialNumber": "555"}
        # ]
        # ---》
        # {
        #     "PickLane1": [{"IOTSerialNumber": 0}],  # 0未PE状态
        #     "PickLane2": [{"IOTSerialNumber": 1}]
        # }
        data = self.datacenter_helper.get_all_iot_from_pick_lanes()
        # 归类数据
        for item in data:
            tmp_dict = {}
            if self.__pick_lane_status.__contains__(item["PickLane"]):
                tmp_dict[item["DeviceSerialNumber"]] = 0
                self.__pick_lane_status[item["PickLane"]].update(tmp_dict)
            else:
                tmp_dict[item["DeviceSerialNumber"]] = 0
                self.__pick_lane_status[item["PickLane"]] = tmp_dict

    @staticmethod
    def parse_iot_status(recv_msg: bytes) -> dict:
        # 这里保存在本地的都是16进制的数据，理论上应该转成方便阅读的，字段代表意义不同
        # 暂时没想好处理的方式，而且存在iot状态是暂时存在本地，方便记录用的，没有实际意义
        # device_serial_number = HexMessageFmt.hex_bytes2hex_str()
        tmp_iot_status_info_dict = dict()

        tmp_iot_status_info_dict["DeviceSerialNumber"] = recv_msg[5:9]
        tmp_iot_status_info_dict["Voltage"] = recv_msg[9:10]
        tmp_iot_status_info_dict["UpCurrent"] = recv_msg[10:11]
        tmp_iot_status_info_dict["MiddleCurrent"] = recv_msg[11:12]
        tmp_iot_status_info_dict["DownCurrent"] = recv_msg[12:13]
        tmp_iot_status_info_dict["InternetStatus"] = recv_msg[13:14]
        tmp_iot_status_info_dict["MotorStatus"] = recv_msg[14:15]
        tmp_iot_status_info_dict["UpSpeed"] = recv_msg[15:17]
        tmp_iot_status_info_dict["MiddleSpeed"] = recv_msg[17:19]
        tmp_iot_status_info_dict["DownSpeed"] = recv_msg[19:21]
        tmp_iot_status_info_dict["PEStatus"] = recv_msg[21:22]
        tmp_iot_status_info_dict["Fault_1"] = recv_msg[22:23]
        tmp_iot_status_info_dict["Fault_2"] = recv_msg[23:24]
        tmp_iot_status_info_dict["Fault_3"] = recv_msg[24:25]
        tmp_iot_status_info_dict["Fault_4"] = recv_msg[25:26]
        tmp_iot_status_info_dict["Fault_5"] = recv_msg[26:27]
        tmp_iot_status_info_dict["Fault_6"] = recv_msg[27:28]
        tm
        
        p_iot_status_info_dict["Fault_7"] = recv_msg[28:29]
        tmp_iot_status_info_dict["Fault_8"] = recv_msg[29:30]
        tmp_iot_status_info_dict["Fault_9"] = recv_msg[30:31]
        tmp_iot_status_info_dict["Fault_10"] = recv_msg[31:32]
        # Task 692717: IOT2006:Communication protocol between IOT and Controller
        tmp_iot_status_info_dict["Fault_11"] = recv_msg[32:33]
        tmp_iot_status_info_dict["Fault_12"] = recv_msg[33:34]
        tmp_iot_status_info_dict["Fault_13"] = recv_msg[34:35]

        iot_status_info_dict = {}
        for (key, value) in tmp_iot_status_info_dict.items():
            iot_status_info_dict[key] = HexMessageFmt.hex_bytes2hex_str(tmp_iot_status_info_dict[key])

        return iot_status_info_dict

    def iot_upload_status(self, recv_msg, is_need_realtime_upload: bool = False):
        iot_status_info = self.parse_iot_status(recv_msg)
        # Task 834246: PickModule: PTL Bind && Light up of Next Wave Logic
        self.set_pick_lane_status(iot_status_info["DeviceSerialNumber"], int(iot_status_info["PEStatus"]))
        # When the dashboard is opened, the iot status is sent up in real time
        if is_need_realtime_upload:
            self.log_helper.info("Dashboard opens the iot status to upload in real time")
            topic = MqttPublishProtocol.Controller2MonitorDashboard
            # 发送16进制的字符串，需要另一端进行处理
            payload = iot_status_info
            self.mqtt_helper.pub(topic, payload)

        iot_status_info = json.dumps(iot_status_info)
        content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + iot_status_info + "\n"
        path_file_name = r"{0}\{1}.log".format(
            settings.TmpFileSetting.Base_IOT_INFO_Status_PATH,
            time.strftime("%Y-%m-%d", time.localtime())
        )

        self.log_helper.custom_log(content, path_file_name)

    async def set_pick_lane_status(self, iot_serial_number: str, pe_status: int):
        for pick_lane_item in self.__pick_lane_status.values():
            if iot_serial_number in pick_lane_item:
                pick_lane_item[iot_serial_number] = pe_status

    def is_all_pick_lane_empty(self) -> bool:
        is_empty = False
        tmp_result_list = list()
        for pick_lane_item in self.__pick_lane_status.values():
            tmp_result_list.append(all(value == 0 for value in pick_lane_item.values()))
        # 判断列表中所有数据都一样, 只需要计算set(List)之后的长度，如果长度是1，我们认为这个List里面的元素只有一个
        is_empty = True if len(set(tmp_result_list)) == 1 else False
        return is_empty

    def is_on_of_pick_lane_empty(self, which_pick_lane: str) -> bool:
        is_empty = False
        pick_lane_iot_status = self.__pick_lane_status.get(which_pick_lane)
        tmp_result_list = list()
        for pick_lane_item in pick_lane_iot_status.values():
            tmp_result_list.append(pick_lane_item)
        is_empty = True if len(set(tmp_result_list)) == 1 else False
        return is_empty


