from sqlalchemy import Column, String, Float, ForeignKey, JSON
from src.db import Base


class WellData(Base):
    __tablename__ = "well_data"
    id = Column(String, primary_key=True)
    inclinometry = Column(JSON)
    d_cas = Column(Float)
    d_tub = Column(Float)
    h_tub = Column(Float)
    wct = Column(Float)
    rp = Column(Float)
    gamma_oil = Column(Float)
    gamma_gas = Column(Float)
    gamma_wat = Column(Float)
    t_res = Column(Float)
    p_wh = Column(Float)
    geo_grad = Column(Float)
    h_res = Column(Float)


class VLP(Base):
    __tablename__ = "vlp"
    vlp = Column(JSON)
    well_id = Column(String, ForeignKey("well_data.id"), primary_key=True)
