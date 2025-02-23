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
                    stage('Setup Git') {
                        steps {
                            script {
                                def gitTool = (OS_TYPE == 'linux') ? 'Git-Linux' : 'Git-Windows'
                                echo "Using Git tool: ${gitTool}"
                                tool name: gitTool, type: 'org.jenkinsci.plugins.git.GitTool'
                            }
                        }
                    }

                    stage('Clone Repository') {
                        steps {
                            git 'https://github.com/MayurBalwani/dirty-login-script.git'
                        }
                    }
                }
            }
        }
    }
}
