document.body.onload = function() {
	randomizeBackground();
	insertReadings();
}

function randomizeBackground() {
	const NUM_BG = 38;
	const BG_PATH = "assets/backgrounds/texture";

	let n = parseInt(1 + Math.random() * NUM_BG).toString();
	document.body.style.backgroundImage = "url(" + BG_PATH + n + ".png)";
}

function insertReadings() {
	let anchor = document.getElementById("readings");
	for (let category in READINGS["categories"])
	{
		let h3 = document.createElement("h3");
		h3.textContent = category;
		h3.className = "category";
		anchor.appendChild(h3);

		READINGS["categories"][category].forEach(reading => {
			if(Object.keys(reading).length == 0)
				return;

			let p = document.createElement("p");
			p.className = "reading";
			
			if(reading['url'] != "") {
				let a = document.createElement("a");
				a.href = reading['url'];
				a.textContent = reading['title'];
				a.style.fontStyle = "italic";
				p.appendChild(a);
			} else {
				p.textContent = reading['title'];
			}

			if(reading['author'] != "") {
				let author = document.createTextNode(" by " + reading['author'])
				p.appendChild(author);
			}

			anchor.appendChild(p);
		})
	}
}