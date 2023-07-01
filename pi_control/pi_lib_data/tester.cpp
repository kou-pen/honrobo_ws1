int main(void){
    /* USER CODE BEGIN 2*/
    //クラス定義
    pid_class motor_pid_1;
    //motor_pwm
    float motor_pwm = 0.0f;
    float re_tim4 = 0.0f;

    motor_pid_1.update_target_spd(100.0f);
    /* USER CODE END 2 */

    /* Infinite loop */
    /* USER CODE BEGIN WHILE */
    while (1)
    {
	    __HAL_TIM_SET_COUNTER(&htim4, 0);
	    HAL_Delay(10);

	    re_tim4 = __HAL_TIM_GET_COUNTER(&htim4);

	    //printf("%f\n\r", re_tim4);

	    motor_pwm = motor_pid_1.motor_calc(re_tim4, MODE_1);

	    printf("%f\n\r", motor_pwm);

	    __HAL_TIM_SET_COMPARE(&htim1, TIM_CHANNEL_1, motor_pwm);
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
    }
    /* USER CODE END 3 */
}