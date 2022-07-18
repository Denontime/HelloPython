/*
 * @Descripttion: Null
 * @version: 1.0
 * @Author: Mar Ping
 * @Date: 2020-10-24 18:42:12
 * @LastEditors: Mar Ping
 * @LastEditTime: 2021-05-27 21:51:40
 */
/*
* 步进电机
* 使用arduino IDE自带的Stepper.h库文件
* 
 */	 
#include <Stepper.h>	 
#define STEPS 120	 
#define One_Step 10
#define AStep -10
#define Start 5   //初始引脚下拉，电平常低
#define End 6     //结束引脚下拉，电平常低
#define OK 1

int angle = 0;        //声明全局变量

Stepper stepper(STEPS, 8, 10, 9, 11);	 //控制引脚定义，分别对应ULN2003的1，2，3，4脚

void setup()
{
  Serial.begin(9600);
  pinMode(Start,INPUT);
  pinMode(End,INPUT);
  stepper.setSpeed(180); // 设置电机每分钟的转速
}	 

void loop()
{
  if(Serial.available()>0){
    char ch = Serial.read();
    if(ch == 'a'){
        Init();
    }
    else if(ch == 'b'){
        Camera_turn();
    }
  }
}

int Init(){
  while(digitalRead(Start)==LOW){//初始
    stepper.step(1);
    delay(1);
  }
  angle = 0;
  Serial.println("OK");
}

int Camera_turn(){
  if(digitalRead(End)==LOW){
    stepper.step(AStep);
    angle++;
    Serial.println(angle);
  }
  else if(digitalRead(End)==HIGH){
    Serial.println("END");
  }

}
