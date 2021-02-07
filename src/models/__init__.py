import bcrypt
from gino.ext.sanic import Gino

db = Gino()


class Chain(db.Model):  # type: ignore
    __tablename__ = "chains"

    name = db.Column(db.String(length=42), primary_key=True)
    chain_type = db.Column(db.String(length=42))
    active = db.Column(db.Boolean(), default=True)
    url = db.Column(db.String())

    @property
    def serialize(self):
        return {
            "name": self.name,
            "type": self.chain_type,
            "active": self.active,
            "url": self.url,
        }


class ContractOracle(db.Model):  # type: ignore
    __tablename__ = "contract_oracles"

    id = db.Column(db.String(length=42), primary_key=True)
    active = db.Column(db.Boolean(), default=True)
    chain = db.Column(db.String(length=42), db.ForeignKey("chains.name"))

    @property
    def serialize(self):
        return {"id": self.id, "active": self.active, "chain": self.chain}


class User(db.Model):  # type: ignore
    __tablename__ = "users"

    email = db.Column(db.String(), primary_key=True)
    password = db.Column(db.LargeBinary())

    def set_password(self, password: bytes) -> None:
        salt = bcrypt.gensalt(rounds=12)
        self.password = bcrypt.hashpw(password, salt)

    def check_password(self, password: bytes) -> bool:
        return bcrypt.checkpw(password, self.password)
