#pragma once

#ifndef PI_CTRL_HPP
#define PI_CTRL_HPP


class pid_class{
private:
    //定数(piなど)
    const float pi = 3.1415926f;

    //計算時使用の定数
    float gain_p = 2000.0f;
    float gain_i = 5.0f;
    float gain_d = 0.0f; //未実装のD制御
    float DELTA_T = 0.01f;
    float max_terget_rad = 6.0f;

    float current_target_rad = 0.0f;
    float before_p = 0.0f; //前回のエラー値
    float integral = 0.0f; //いんてぐらる

    //motor_calc関数から使うこと
    float pi_calc_rad(float);
    float re_convert_rad(float);

public:
    void update_target_spd(float);
    float motor_calc(float, int);
    float re_data_change(float, int);
};

#endif
