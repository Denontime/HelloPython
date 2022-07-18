<!--
 * @Descripttion: Null
 * @version: 1.0
 * @Author: Mar Ping
 * @Date: 2020-04-06 23:56:27
 * @LastEditors: Mar Ping
 * @LastEditTime: 2020-10-29 20:51:33
 -->

# 硬件接口模块v1.0

·**硬件模块部分由小帅编辑**

    name: find_port()
    test: test font
    msg: 串口查找函数，查找并返回计算机上的列表
    param {*}None
    return {*找到串口返回串口列表，未找到串口返回False}

    name: start_port(ports,speed,timex)
    test: test font
    msg: 端口打开函数
    param {*str 端口名称} ports
    param {*int 波特率} speed
    param {*int 生命周期} timex
    return {*端口对象}

    name: open_serial(com)
    test: test font
    msg: 串口打开函数
    param {*str 'COM4'} com
    return {*成功返回端口对象，失败返回False}

    name: stepper_turn(port)
    test: test font
    msg: 电机旋转函数，转到指定角度
    param {*端口对象} port
    return {*None}

    name: stepper_init(port)
    test: test font
    msg: 电机初始化函数
    param {*端口对象} port
    return {*None}

    name: port_close(port)
    test: test font
    msg: 端口关闭函数
    param {*端口对象} port
    return {*None}
