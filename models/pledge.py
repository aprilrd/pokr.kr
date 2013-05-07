# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, Unicode, UnicodeText
from database import Base

class Pledge(Base):
    __tablename__ = 'pledge'

    id = Column(Integer, autoincrement=True, primary_key=True)
    candidacy_id = Column(Integer, ForeignKey('candidacy.id'), nullable=False)
    pledge = Column(Unicode(128))
    description = Column(UnicodeText)
