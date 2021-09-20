class UserModel():

    users=[]
    
    """
    Class for the user operations
    """
    def __init__(self,username,password,task,tasktime,break_time):

        self.id=len(UserModel.users)+1
        self.username=username
        self.task=task
        self.password=password
        self.tasktime=tasktime
        self.break_time=break_time
        self.task_completed=False


    def save_user(self):
        """
        Method to register a user instance and update the data structure
        """
        user_record=dict(
            id=self.id,
            username=self.username,
            task=self.task,
            password = self.password,
            tasktime=self.tasktime,
            break_time=self.break_time,
            task_completed=self.task_completed
        )

        self.users.append(user_record)
        
        