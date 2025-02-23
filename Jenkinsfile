pipeline {
    agent none

    stages {
        stage('Run on Multiple OS') {
            matrix {
                axes {
                    axis {
                        name 'OS_TYPE'
                        values 'linux', 'windows'
                    }
                }
                agent { label OS_TYPE }

                stages {

                    stage('Clone Repository') {
                        steps {
                            git 'https://github.com/MayurBalwani/dirty-login-script.git'
                        }
                    }

                    stage('Creating Virtual Environment') {
                        steps {
                            script {
                                if (OS_TYPE == 'linux') {
                                    sh 'python3 -m venv venv'
                                } else {
                                    bat 'python -m venv venv'
                                }
                            }
                        }
                    }

                    stage('Install Requirements') {
                        steps {
                            script {
                                if (OS_TYPE == 'linux') {
                                    sh '''
                                    . ./venv/bin/activate
                                    pip install -r requirements.txt
                                    '''
                                } else {
                                    bat '''
                                    cd venv\\Scripts && call activate && cd ../..
                                    pip install -r requirements.txt
                                    '''
                                }
                            }
                        }
                    }

                    stage('Run Script') {
                        steps {
                            script {
                                if (OS_TYPE == 'linux') {
                                    sh '''
                                    . ./venv/bin/activate
                                    python main.py
                                    '''
                                } else {
                                    bat '''
                                    cd venv\\Scripts && call activate && cd ../..
                                    python main.py
                                    '''
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
