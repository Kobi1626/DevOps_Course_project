pipeline {
    agent any
    
    triggers {
        pollSCM('H/30 * * * *')
    }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', artifactDaysToKeepStr: '5'))
    }
    
    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/Kobi1626/DevOps_Course_project.git'
            }
        }
        
        stage('Clean Environment1') {
            steps {
                sh 'nohup python3 clean_environment.py &'
            }
        } 
                        
        
        stage('Install Requirements') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        } 
        
        stage('Run Backend Server') {
            steps {
                sh 'nohup python3 rest_app.py &'
            }
        }
        
        stage('Run Backend Testing') {
            steps {
                sh 'python3 backend_testing.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t rest_app:latest .'
            }
        }
        
        stage('Push Docker Image') {
            steps {
                sh 'docker push Kobi1626/rest_app:latest'
            }
        }
        
        stage('Set Compose Image Version') {
            steps {
                sh 'echo "IMAGE_TAG=${BUILD_NUMBER}" > .env'
            }
        }
        
        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        
        stage('Test Dockerized App') {
            steps {
                sh 'python3 docker_backend_testing.py'
            }
        }
        
        stage('Clean Environment') {
            steps {
                sh 'docker-compose down'
                sh 'docker rmi rest_app:latest'
            }
        }
    }
}
