node {
    def isLinux = isUnix()  // Automatically detect OS type

    stage('Clone Repository') {
        if (isLinux) {
            sh '''
            rm -rf ./dirty-login-script
            git clone https://github.com/MayurBalwani/dirty-login-script.git'''
        } else {
            bat '''
            rmdir /s /q "dirty-login-script"
            git clone https://github.com/MayurBalwani/dirty-login-script.git'''
        }
    }

    stage('Creating the virtual environment') {
        if (isLinux) {
            sh 'python3 -m venv venv'
        } else {
            bat 'python -m venv venv'
        }
    }

    stage('Install requirements') {
        if (isLinux) {
            sh '''
            . ./venv/bin/activate
            cd ./dirty-login-script
            pip install -r requirements.txt
            '''
        } else {
            bat '''
            cd venv\\Scripts && call activate
            cd ../.. && cd ./dirty-login-script && pip install -r requirements.txt
            '''
        }
    }

    stage('Run script') {
        if (isLinux) {
            sh '''
            . ./venv/bin/activate
            cd ./dirty-login-script
            // python main.py
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
