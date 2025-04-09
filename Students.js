const student = {
    name: "Андрій",
    specialty: "Комп'ютерні науки",
    averageGrade: 98,
    missedClasses: 1,

    showInfo: function() {
        return `
      <strong>Ім'я:</strong> ${this.name}<br>
      <strong>Спеціальність:</strong> ${this.specialty}<br>
      <strong>Середній бал:</strong> ${this.averageGrade}<br>
      <strong>Пропущено занять:</strong> ${this.missedClasses}<br><hr>
    `;
    }
};

const student2 = {
    name: "Олена",
    specialty: "Веб Дизайн",
    averageGrade: 98,
    missedClasses: 12
};

const student3 = {
    name: "Ігор",
    specialty: "Механіка",
    averageGrade: 79,
    missedClasses: 5
};

function ShowAllStudents () {
    const output = document.getElementById("output");
    output.innerHTML = '';

    output.innerHTML += student.showInfo.call(student2);
    output.innerHTML += student.showInfo.apply(student3);

    const ShowOriginal = student.showInfo.bind(student);
    output.innerHTML += ShowOriginal();
}