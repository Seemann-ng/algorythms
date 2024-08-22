class Publisher:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def getInfo(self):
        return f"{self.name} ({self.location})"

    def publish(self, message: str):
        print(f"Preparing {message} for being published at {self.getInfo()}")


class BookPublisher(Publisher):
    def __init__(self, name: str, location: str, num_authors: int):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, author: str, title: str):
        print(f"Presenting the manuscript '{title}' written by {author} to the publishing house {self.getInfo()}")


class NewspaperPublisher(Publisher):
    def __init__(self, name: str, location: str, num_pages: int):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, headline: str):
        print(
            f"Printing the latest issue with headline '{headline}' on the main page at the publishing house {self.getInfo()}")


publisher = Publisher("ABC Press", "New-York, NY")
book_publisher = BookPublisher("GF Flammarion", "Paris", 52)
newspaper_publisher = NewspaperPublisher("NY Times", "New-York, NY", 12)

publisher.publish("Writer's handbook")
book_publisher.publish("Platon", "La République")
newspaper_publisher.publish("New version of Midjourney to be paid")
