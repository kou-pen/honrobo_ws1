#include "pi_ctrl.hpp"

//単位は(rad/s)
float pid_class::pi_calc_rad(float current_rad, float terget_rad){
    float result_p = 0, result_i = 0;
    float calc_p = 0;
    
    //計算
    calc_p = terget_rad - current_rad;
    integral += (calc_p + before_p) / 2.0f * DELTA_T;

    //ゲインとかけてみる
    result_p = gain_p * calc_p;
    result_i = gain_i * integral;

    //次回計算用に今回のエラー値を保存
    before_p = calc_p;

    return result_p + result_i;
}

//エンコーダーちゃんからのデータはここに入れて、(rad/s)にする
float pid_class::re_convert_rad(float current_data){
    float rad_per_sec = 0;

    rad_per_sec = ((current_data * pi) / 1024.0f) / DELTA_T;
    
    return rad_per_sec;
}

//ゲインを変えたいときに
void pid_class::gain_setup(float new_p_gain, float new_i_gain, float new_d_gain){
    gain_p = new_p_gain;
    gain_i = new_i_gain;
    gain_d = new_d_gain;

    return;
}

//目標速度設定を変えたいときに
void pid_class::terget_setup(float new_terget_rad){
    terget_rad = new_terget_rad;

    return;
}