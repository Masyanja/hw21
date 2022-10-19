from entity.exception import InvalidRequest


class Request:

    def __init__(self, request: str):
        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise InvalidRequest

        self.amount = int(splitted_request[1])
        self.product = splitted_request[2]
        self.departure = splitted_request[4]
        self.destination = splitted_request[6]
