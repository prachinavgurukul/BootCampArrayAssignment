// elements = [1,3,5,7,10,7,1,8,12]
// removeduplicate=[]
// for (i of elements){
//     if(!removeduplicate.includes(i)){
//         removeduplicate.push(i)
//     }
// }
// console.log(removeduplicate)


const students = [
    {id:'s1',
    marks:
    {
    'physics':100,
    'maths':80
    }
    },
    {id:'s2',
    marks:
    {
    'physics':60,
    'maths':40
    }
    },
    {id:'s3',
    marks:
    {
    'physics':70,
    'maths':90
    }
    },
    {id:'s4',
    marks:
    {
    'physics':50,
    'maths':85
    }
    },
    {id:'s4',
    marks:
    {
    'physics':30,
    'maths':75
    }
    }
    ];
    sum=0
    for(i of students){
        sum+=i.marks.physics
        avg_of_physics=sum/students.length
    }
    console.log(avg_of_physics)
    
