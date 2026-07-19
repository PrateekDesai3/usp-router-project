from fastapi import APIRouter
from app.tr369.message_processor import USPMessageProcessor

router = APIRouter()

processor = USPMessageProcessor()


@router.post("/usp")

def usp(request: dict):

    return processor.process(request)