#pragma once

class pid_class{
private:
    //定数(piなど)
    const float pi = 3.1415926f;
    const float default_gain_p = 2000.0f;
    const float default_gain_i = 5.0f;
    const float default_gain_d = 0.0f;
    const float default_delta_t = 0.01f;
    const float default_target_rad = 0.0f;

    //計算時使用の定数(gain_setup関数で変更可能とする)
    float gain_p = default_gain_p;
    float gain_i = default_gain_i;
    float gain_d = default_gain_d; //未実装のD制御
    float DELTA_T = default_delta_t;
    float terget_rad = default_target_rad;

    float before_p = 0.0f; //前回のエラー値
    float integral = 0.0f; //いんてぐらる

public:
    float pi_calc_rad(float, float);
    float re_convert_rad(float);
    void gain_setup(float, float, float);
    void terget_setup(float);
};