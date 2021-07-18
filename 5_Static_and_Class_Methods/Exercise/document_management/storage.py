from document_management.category import Category
from document_management.document import Document
from document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def extract(self, obj_id, type_obj: [Category, Topic, Document]):
        mapper = {Category: self.categories, Topic: self.topics, Document: self.documents}
        index_with_obj = [(ind, o) for ind, o in enumerate(mapper[type_obj]) if o.id == obj_id][0]
        return index_with_obj

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
        return

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
        return

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
        return

    def edit_category(self, category_id: int, new_name: str):
        category_data: Category = Storage.extract(self, category_id, Category)
        if category_data:
            index, category = category_data
            category.name = new_name
            self.categories[index] = category
        return

    def edit_topic(self, topic_id: int,  new_topic: str, new_storage_folder: str):
        topic_data: Topic = Storage.extract(self, topic_id, Topic)
        if topic_data:
            index, topic = topic_data
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder
            self.topics[index] = topic
        return

    def edit_document(self, document_id: id, new_file_name: str):
        document_data: Document = Storage.extract(self, document_id, Document)
        if document_data:
            index, document = document_data
            document.file_name = new_file_name
            self.documents[index] = document
        return

    def delete_category(self, category_id: int):
        category_data = Storage.extract(self, category_id, Category)
        if category_data:
            index, _ = category_data
            del self.categories[index]
        return

    def delete_topic(self, topic_id: int):
        topic_data = Storage.extract(self, topic_id, Topic)
        if topic_data:
            index, _ = topic_data
            del self.topics[index]
        return

    def delete_document(self, document_id: int):
        document_data = Storage.extract(self, document_id, Document)
        if document_data:
            index, _ = document_data
            del self.documents[index]
        return

    def get_document(self, document_id: int):
        document_data = Storage.extract(self, document_id, Document)
        if document_data:
            _, document = document_data
            return document

    def __repr__(self):
        result = '\n'.join([repr(d) for d in self.documents])
        return result


if __name__ == "__main__":
    c1 = Category(1, "work")
    t1 = Topic(1, "daily tasks", "C:\\work_documents")
    d1 = Document(1, 1, 1, "finilize document_management")

    d1.add_tag("urgent")
    d1.add_tag("work")

    storage = Storage()
    storage.add_category(c1)
    storage.add_topic(t1)
    storage.add_document(d1)

    print(c1)
    print(t1)
    print(storage.get_document(1))
    print(storage)