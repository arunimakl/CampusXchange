// -------- Books --------
function showDetails(title, author, dept, owner, price, condition, contact){
    alert(`Title: ${title}\nAuthor: ${author}\nDept: ${dept}\nOwner: ${owner}\nPrice: ${price}\nCondition: ${condition}\nContact: ${contact}`);
}

const searchInput = document.getElementById('searchInput');
if(searchInput){
    searchInput.addEventListener('keyup', function(){
        const query = this.value.toLowerCase();
        const cards = document.querySelectorAll('#bookList .card, #tutorList .card, #skillList .card');
        cards.forEach(card=>{
            const text = card.innerText.toLowerCase();
            card.style.display = text.includes(query)?'block':'none';
        });
    });
}

const deptFilter = document.getElementById('deptFilter');
if(deptFilter){
    deptFilter.addEventListener('change', function(){
        const selected = this.value.toLowerCase();
        const cards = document.querySelectorAll('#bookList .card');
        cards.forEach(card=>{
            const dept = card.querySelector('p:nth-child(3)').innerText.toLowerCase();
            card.style.display = (!selected || dept.includes(selected))?'block':'none';
        });
    });
}

// -------- Tutors --------
function showTutor(name, skill, rate, days, location){
    alert(`Name: ${name}\nSkill: ${skill}\nRate: ${rate}\nDays: ${days}\nLocation: ${location}`);
}

// -------- Skills --------
function showSkill(skill, owner, experience, contact){
    alert(`Skill: ${skill}\nOwner: ${owner}\nExperience: ${experience}\nContact: ${contact}`);
}