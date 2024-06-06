from datetime import datetime
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


# Воркеры для очистки неактивных комнат
async def clean_old_rooms():
    while True:
        now = datetime.now()
        inactive_threshold = now - timedelta(hours=1)  # Удалять комнаты, неактивные более 1 часа
        to_delete = [room_id for room_id, room in ROOMS_DATABASE.items() if room.last_activity < inactive_threshold]
        for room_id in to_delete:
            del ROOMS_DATABASE[room_id]
            print(f"Deleted room {room_id} due to inactivity.")
        await asyncio.sleep(3600)  # Запускать каждую 1 час

@app.on_event("startup")
async def startup_event():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(clean_old_rooms, 'interval', hours=1)  # Запускать каждую 1 час
    scheduler.start()

    # Дополнительно, можно сразу запустить задачу
    asyncio.create_task(clean_old_rooms())