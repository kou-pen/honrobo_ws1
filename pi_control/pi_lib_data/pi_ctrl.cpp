#include "pi_ctrl.hpp"

//単位は(rad/s)
float pid_class::pi_calc_rad(float current_rad){
    float result_p = 0, result_i = 0;
    float calc_p = 0;
    
    //ここで直接値をいじっても、変化しなかった
    //float current_target = 3.0f;

    //計算
    calc_p = current_target_rad - current_rad;
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

//現在の目標速度設定(コントローラーの入力をここで目標速度に変換する)
void pid_class::update_target_spd(float spd_rate){
    current_target_rad = max_terget_rad * (spd_rate * 0.01f);
    //spd_rateは、コントローラーから得た入力を計算して、最大入力との割合で出す予定
    //現在は100.0fを代入
}

//エンコーダーの入力から、PWMの値を求める(この前に、delayを入れておくこととする)
float pid_class::motor_calc(float current_data, int calc_mode){
    float rad_per_sec = 0.0f, result_motor_pwm = 0.0f;

    current_data = pid_class::re_data_change(current_data, calc_mode);

    rad_per_sec = pid_class::re_convert_rad(current_data);

    result_motor_pwm = pid_class::pi_calc_rad(rad_per_sec);

    if(result_motor_pwm < 0.0f){
        result_motor_pwm = 0.0f;
    }else if(result_motor_pwm > 65535.0f){
        result_motor_pwm = 65535.0f;
    }

    return result_motor_pwm;
}

//ここが怪しいのかな
float pid_class::re_data_change(float re_tim, int calc_mode){
	if(calc_mode == 0){
		if(re_tim > 32767){
			re_tim -= 65535;
		}
	}else if(calc_mode == 1){
		if(re_tim < 32767){
			re_tim *= -1;
		}else{
			re_tim -= 65535;
			re_tim *= -1;
		}
	}

	return re_tim;
}
