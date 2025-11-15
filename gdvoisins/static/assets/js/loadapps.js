const menuBtn = document.getElementById('menuBtn');
const appMenu = document.getElementById('appMenu');
const overlay = document.getElementById('overlay');
const appGrid = document.getElementById('appGrid');

function getTextColor(hex) {
    // rgba = rgba.match(/\d+/g);
    // r = rgba[0];
    // g = rgba[1];
    // b = rgba[2];
    r = parseInt(hex.slice(1, 3), 16);
    g = parseInt(hex.slice(3, 5), 16);
    b = parseInt(hex.slice(5, 7), 16);
    // if ((r * 0.299) + (g * 0.587) + (b * 0.114) > 186) {
    if ((r * 0.299) + (g * 0.587) + (b * 0.114) > 127) {
        return 'black';
    } else {
        return 'white';
    }
}

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    loadApps();
});



// Load apps from JSON data
function loadApps() {
    appsData.groups.forEach(group => {
        // const groupDiv = document.createElement('div');
        // groupDiv.className = 'app-group';

        // const groupLabel = document.createElement('div');
        // groupLabel.className = 'group-label';
        // groupLabel.textContent = group.label;
        // // groupDiv.appendChild(groupLabel);
        // appGrid.appendChild(groupLabel);

        n = group.apps.length
        i = 0;

        group.apps.forEach(app => {
            const appItem = document.createElement('a');
            i++;
            label = "";
            if (i == 1) {
                extraClass = "app-item-first";
                // label = `
                // <label for="${app.id}">
                //     ${group.label}
                // </label>
                // `;
            } else if (i == n) {
                extraClass = "app-item-last";
            } else {
                extraClass = "app-item-middle";
            }
            appItem.href = app.url;
            appItem.className = "app-item " + extraClass;
            app.textColor = getTextColor(app.color);
            app.letter = "";
            appNames = app.appName.split(' ');
            for (iName in appNames) {
                if (appNames[iName].charAt(0) == "(") {
                    if (appNames[iName].length > 1) {
                        app.letter += appNames[iName].charAt(1);
                    }
                } else {
                    app.letter += appNames[iName].charAt(0);
                }
            };


            docHTML = "";
            if (app.docurl && app.docurl != "") {
                docHTML = `
                <form action="${app.docurl}" class="app-documentation"><input type="submit" value="ℹ️"/></form>
                `;
            }
            appItem.innerHTML = `
                        ${label}
                        <div class="app-card" id="${app.id}">
                            <div class="app-front">
                                <div class="app-icon" style="background: ${app.color}; color:${app.textColor}">${app.letter}</div>
                                <div class="app-name">${app.appName}</div>
                                ${docHTML}
                            </div>
                            <div class="app-back">
                                    <div class="app-name">${app.appName}</div>
                                    <div class="app-description">${app.description}</div>
                                ${docHTML}
                                    <!-- <div class="group-label">${group.label}</div> -->
                            </div>
                        </div>
                
                    `;

            // appItem.addEventListener('click', (e) => {
            //     e.preventDefault();
            //     toggleMenu();    
            //     console.log(`Clicked: ${app.appName}`);
            // });

            // groupDiv.appendChild(appItem);


            appGrid.appendChild(appItem);
            if (i == n) {
                flexBreak = document.createElement('div');
                flexBreak.className = 'app-flex-break';
                appGrid.appendChild(flexBreak);
            }
        });

        // appGrid.appendChild(groupDiv);
    });
}

function toggleMenu() {
    appMenu.classList.toggle('active');
    overlay.classList.toggle('active');
}

menuBtn.addEventListener('click', toggleMenu);
overlay.addEventListener('click', toggleMenu);