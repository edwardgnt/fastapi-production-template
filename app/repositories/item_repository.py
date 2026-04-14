from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class ItemRepository:
    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
    ) -> list[Item]:
        query = db.query(Item)

        if search: 
            query = query.filter(Item.name.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, item_id: int) -> Item | None:
        return db.query(Item).filter(Item.id == item_id).first()

    def create(self, db: Session, item_in: ItemCreate) -> Item:
        item = Item(name=item_in.name, description=item_in.description)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def update(self, db: Session, item: Item, item_in: ItemUpdate) -> Item:
        if item_in.name is not None:
            item.name = item_in.name
        if item_in.description is not None:
            item.description = item_in.description

        db.commit()
        db.refresh(item)
        return item

    def delete(self, db: Session, item: Item) -> None:
        db.delete(item)
        db.commit()