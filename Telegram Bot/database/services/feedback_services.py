from ..models.feedback_model import Feedback, feedbacks_collection

async def get_feedbacks() -> list[Feedback]:
    feedbacks = feedbacks_collection.find()
    return [Feedback(**u) async for u in feedbacks]

async def get_feedback_by_id(id: int) -> Feedback or None:
    feedback = await feedbacks_collection.find_one({'_id': id})
    return Feedback(**feedback) if feedback else None

async def create_feedback(id: int, **kwargs) -> Feedback:
    feedback = await feedbacks_collection.insert_one({'_id': id, **kwargs})
    return await get_feedback_by_id(id)

async def update_feedback(id: int, **kwargs) -> Feedback or None:
    feedback = await feedbacks_collection.find_one_and_update(
        {'_id': id},
        {'$set': kwargs},
        return_document=True
    )
    return await get_feedback_by_id(id)

async def delete_feedback_by_id(id: int) -> bool:
    result = await feedbacks_collection.delete_one({'_id': id})
    return result.deleted_count > 0
