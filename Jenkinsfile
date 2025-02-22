node(params.OS_TYPE){
        stage('Creating the virtual environment') {
           if(params.OS_TYPE=='windows')
           {
            bat 'python -m venv venv'
           }
           else{
            sh 'python3 -m venv venv'   
           }
        }

        stage('Install requirements') {
            if (params.OS_TYPE=='windows')
            {
                bat '''
                cd venv\\Scripts && call activate
                cd ../.. && cd ./dirty-login-script && pip install -r requirements.txt
                '''
            }
            else{
                sh '''
                . ./venv/bin/activate
                cd ./dirty-login-script
                pip install -r requirements.txt
                '''    
            }
        }

        stage('Run script') {
            if(params.OS_TYPE=='windows'){
                bat '''
                cd venv\\Scripts && call activate && cd ../..
                python main.py
                '''
            }
            else{
                sh '''
                . ./venv/bin/activate
                '''
            }
        }
}
