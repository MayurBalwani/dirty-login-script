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
                agent { label OS_TYPE }  // Runs sequentially per OS
                
                stages {
                    stage('Clone Repository') {
                        steps {
                            script {
                                if (OS_TYPE == 'linux') {
                                    sh '''
                                    rm -rf ./dirty-login-script
                                    git clone https://github.com/MayurBalwani/dirty-login-script.git
                                    '''
                                } else {
                                    bat '''
                                    rmdir /s /q "dirty-login-script"
                                    git clone https://github.com/MayurBalwani/dirty-login-script.git
                                    '''
                                }
                            }
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
                                    cd ./dirty-login-script
                                    pip install -r requirements.txt
                                    '''
                                } else {
                                    bat '''
                                    cd venv\\Scripts && call activate
                                    cd ../.. && cd ./dirty-login-script
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
                                    cd ./dirty-login-script
                                    python main.py
                                    '''
                                } else {
                                    bat '''
                                    cd venv\\Scripts && call activate && cd ../..
                                    cd ./dirty-login-script
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
