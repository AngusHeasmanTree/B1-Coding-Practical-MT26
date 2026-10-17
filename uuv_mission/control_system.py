"""Proportional-derivative control for the UUV mission.

After initialising the object with the required constants the action_calculator method calculates the control action from the target and actual positions.
The constants relating to proportional and derivative control may be set when initialising the class.
In order to prevent indexing errors a proportional-only control is used on the first time step.

Typical usage example:
    Submarine_PDController = PD_Controller(0.15,0.6)
    action = Submarine_PDController.action_calculator()
"""

class PD_Controller:
    def __init__(self, K_P, K_D):
        self.K_P = K_P
        self.K_D = K_D

    def action_calculator(self,t,target_position,actual_position):
        
        error_position = target_position - actual_position[:, 1]
        action = self.K_P*(error_position[t]) + self.K_D*(error_position[t]-error_position[t-1])

        return action