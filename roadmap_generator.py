roadmaps={
    "Python":[
        "Learn Python syntax and data types.",
        "Practice loops, functions and OOP.",
        "Solve Python coding problems.",
        "Build small Python projects."
    ],
    "Java":[
        "Learn Java fundamentals.",
        "Practice OOP concepts.",
        "Study collections and exception handling.",
        "Build Java applications."
    ],
    "C++":[
        "Learn C++ syntax and OOP.",
        "Practice STL and pointers.",
        "Solve DSA problems.",
        "Build console applications."
    ],
    "SQL":[
        "Learn SQL queries.",
        "Practice joins and subqueries.",
        "Study normalization.",
        "Build database projects."
    ],
    "DBMS":[
        "Study ER diagrams.",
        "Learn normalization.",
        "Practice SQL queries.",
        "Understand transactions and indexing."
    ],
    "Machine Learning":[
        "Learn supervised learning.",
        "Study regression and classification.",
        "Practice using Scikit-learn.",
        "Build ML projects."
    ],
    "Deep Learning":[
        "Learn neural networks.",
        "Study TensorFlow or PyTorch.",
        "Practice CNNs and RNNs.",
        "Build deep learning projects."
    ],
    "TensorFlow":[
        "Learn TensorFlow basics.",
        "Build neural networks.",
        "Train image classification models.",
        "Deploy TensorFlow projects."
    ],
    "PyTorch":[
        "Learn tensors and autograd.",
        "Build neural networks.",
        "Train deep learning models.",
        "Practice real-world projects."
    ],
    "HTML":[
        "Learn HTML elements.",
        "Create responsive web pages.",
        "Build portfolio websites.",
        "Practice semantic HTML."
    ],
    "CSS":[
        "Learn CSS selectors.",
        "Study Flexbox and Grid.",
        "Build responsive layouts.",
        "Practice animations."
    ],
    "JavaScript":[
        "Learn JavaScript basics.",
        "Practice DOM manipulation.",
        "Study ES6 features.",
        "Build interactive websites."
    ],
    "React":[
        "Learn React components.",
        "Study hooks and routing.",
        "Build React projects.",
        "Connect React with APIs."
    ],
    "Node.js":[
        "Learn Node.js basics.",
        "Build REST APIs.",
        "Connect databases.",
        "Deploy backend projects."
    ],
    "Docker":[
        "Learn Docker fundamentals.",
        "Create Docker images.",
        "Study Docker Compose.",
        "Deploy applications using Docker."
    ],
    "AWS":[
        "Learn AWS core services.",
        "Study EC2 and S3.",
        "Deploy cloud applications.",
        "Practice AWS projects."
    ],
    "Git":[
        "Learn Git commands.",
        "Practice branching and merging.",
        "Use GitHub repositories.",
        "Collaborate on projects."
    ],
    "GitHub":[
        "Create repositories.",
        "Practice commits and pull requests.",
        "Collaborate with teams.",
        "Build an online portfolio."
    ]
}

def get_roadmap(missing_skills):
    roadmap=[]
    for skill in missing_skills:
        if skill in roadmaps:
            roadmap.append(roadmaps[skill])
        else:
            roadmap.append([
                f"Learn the fundamentals of {skill}.",
                f"Practice {skill} through projects.",
                f"Build real-world applications using {skill}.",
                f"Add {skill} projects to your resume."
            ])
    return roadmap
