import datetime

class Feedback():

    def __init__(self,
                    id_feedback: str,
                    message: str,
                    date_ecriture: datetime.date ) -> None:
        self.__id_feedback = id_feedback
        self.__message = message
        self.__date_ecriture = date_ecriture

    @property
    def id_feedback(self):
        return self.__id_feedback

    @id_feedback.setter
    def id_feedback(self, value):
        self.__id_feedback = value   

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def date_ecriture(self):
        return self.__date_ecriture

    @date_ecriture.setter
    def date_ecriture(self, value):
        self.__date_ecriture = value        