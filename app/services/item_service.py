from sqlalchemy.orm import Session

from app.models.item import Item
from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemCreate, ItemUpdate


class ItemService:
    def __init__(self) -> None:
        self.repository = ItemRepository()

    def get_items(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
    ) -> list[Item]:
        return self.repository.get_all(db, skip=skip, limit=limit, search=search)

    def get_item(self, db: Session, item_id: int) -> Item | None:
        return self.repository.get_by_id(db, item_id)

    def create_item(self, db: Session, item_in: ItemCreate) -> Item:
        return self.repository.create(db, item_in)

    def update_item(self, db: Session, item: Item, item_in: ItemUpdate) -> Item:
        return self.repository.update(db, item, item_in)

    def delete_item(self, db: Session, item: Item) -> None:
        self.repository.delete(db, item)
