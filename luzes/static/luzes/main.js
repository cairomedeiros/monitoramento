// luzes/static/luzes/js/scripts.js

function listarLuzes() {
    fetch('listar_luzes/')
        .then(response => response.json())
        .then(data => {
            const luzesList = document.getElementById('luzes-list');
            luzesList.innerHTML = '';
            data.forEach(luz => {
                const luzItem = document.createElement('div');
                luzItem.textContent = `ID: ${luz.id}, Status: ${luz.status}, Brilho: ${luz.brilho}`;
                luzesList.appendChild(luzItem);
            });
        });
}

function controlarLuz(event) {
    event.preventDefault();
    const luzId = document.getElementById('luz-id').value;
    const action = document.getElementById('action').value;

    fetch(`luz/${luzId}/${action}/`)
        .then(response => response.json())
        .then(data => {
            alert(`Luz ${luzId} está agora ${data.status ? 'ligada' : 'desligada'}`);
        });
}

function setBrilho(event) {
    event.preventDefault();
    const luzId = document.getElementById('luz-id-brilho').value;
    const brilho = document.getElementById('brilho').value;

    fetch(`brilho/${luzId}/${brilho}/`)
        .then(response => response.json())
        .then(data => {
            alert(`Brilho da luz ${luzId} foi ajustado para ${data.brilho}`);
        });
}
