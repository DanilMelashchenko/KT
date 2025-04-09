const student = {
    name: "Андрій",
    specialty: "Комп'ютерні науки",
    averageGrade: 98,
    missedCkasses: 1,

    showInfo: function() {
        console.log(`Ім'я: ${this.name}`);
        console.log(`Спеціальність: ${this.specialty}`);
        console.log(`Середній бал: ${this.averageGrade}`);
        console.log(`Пропущенно занять: ${this.missedCkasses}`);
        console.log(`----------------------------`);
    }
};

const student2 = {
    name: "Олена",
    specialty: "Веб Дизайн",
    averageGrade: 88,
    missedCkasses: 12
};

const student3 = {
    name: "Ігор",
    specialty: "Механіка",
    averageGrade: 79,
    missedCkasses: 5
};

student.showInfo.call(student2);
student.showInfo.apply(student3);

const showOriginalStudent = student.showInfo.bind(student);
showOriginalStudent ();