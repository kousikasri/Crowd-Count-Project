let points = [];
const video = document.getElementById("video");

video.addEventListener("click", e => {
    const rect = video.getBoundingClientRect();
    points.push({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
    });
    drawDot(e.clientX - rect.left, e.clientY - rect.top);
});

function drawDot(x, y) {
    const dot = document.createElement("div");
    dot.style = `
        position:absolute;
        left:${x}px;
        top:${y}px;
        width:6px;
        height:6px;
        background:red;
        border-radius:50%;
    `;
    document.body.appendChild(dot);
}

function saveZone() {
    const name = document.getElementById("zoneName").value;

    fetch("http://127.0.0.1:5000/zones", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({ name, points })
    }).then(() => {
        alert("Zone saved");
        points = [];
        loadZones();
    });
}

function loadZones() {
    fetch("http://127.0.0.1:5000/zones")
    .then(r => r.json())
    .then(zones => {
        const ul = document.getElementById("zoneList");
        ul.innerHTML = "";
        zones.forEach(z => {
            ul.innerHTML += `
              <li>
                ${z.name}
                <button onclick="deleteZone('${z.id}')">❌</button>
              </li>
            `;
        });
    });
}

function deleteZone(id) {
    fetch(`http://127.0.0.1:5000/zones/${id}`, {method:"DELETE"})
    .then(loadZones);
}

loadZones();
