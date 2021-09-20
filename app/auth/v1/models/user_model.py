from datetime import datetime,date

class UserModel():

    users=[]
    
    """
    Class for the user operations
    """
    def __init__(self,username,task,tasktime,break_time):

        self.id=len(UserModel.users)+1
        self.username=username
        self.task=task
        self.tasktime=tasktime
        self.break_time=break_time
        self.task_completed=False
        self.task_start=datetime.now().strftime("%H:%M:%S")
        # self.task_start_string= self.task_start.strftime("%d-%b-%Y (%H:%M:%S.%f)")


    def save_user(self):
        """
        Method to register a user instance and update the data structure
        """
        user_record=dict(
            id=self.id,
            username=self.username,
            task=self.task,
            tasktime=self.tasktime,
            break_time=self.break_time,
            task_completed=self.task_completed,
            task_start=self.task_start
        )

        self.users.append(user_record)
        
        