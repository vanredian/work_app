// document.getElementById('createJoinBtn').addEventListener('click', function() {
//             const uuid = document.getElementById('uuidInput').value;
//             if (uuid) {
//                 // Логика для присоединения к комнате с данным UUID
//                 console.log('Join button clicked with UUID:', uuid);
//             } else {
//                 // Логика для создания комнаты
//                 console.log('Create button clicked');
//             }
//         });

//         document.getElementById('syncBtn').addEventListener('click', function() {
//             // Логика для синхронизации
//             console.log('Sync button clicked');
//         });



document.getElementById('createJoinBtn').addEventListener('click', function () {
    const uuid = document.getElementById('uuidInput').value;
    if (uuid) {
        // Logic to join room with the provided UUID
        console.log('Join button clicked with UUID:', uuid);
        fetch(`/room/${uuid}`, {
            method: 'POST',
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
    } else {
        // Logic to create a new room
        console.log('Create button clicked');
        fetch('/room', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: "New Room" }),
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
    }
});

document.getElementById('syncBtn').addEventListener('click', function () {
    // Logic to synchronize
    console.log('Sync button clicked');
    fetch('/rooms', {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
});