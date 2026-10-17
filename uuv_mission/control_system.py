def PD_contoller(t,target_position,actual_position):
    K_P = 0.15
    K_D = 0.6

    error_position = target_position - actual_position

    # The desired PD controller uses an index of t-1. This may cause an indexing error on the first step, 
    # so a proportional controller is used in the first step instead
    if t >= 1:
        action = K_P*(error_position[t]) +K_D*(error_position[t]-error_position[t-1])
    else:
        action = K_P*(error_position[t])

    return action
