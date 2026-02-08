
import os

template_path = 'project-template.html'

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Fix navbar links to point to index.html from subdirectories
template = template.replace('href="#', 'href="../index.html#')
template = template.replace('href="index.html', 'href="../index.html')

# Fix asset paths for subdirectories
template = template.replace('src="images/', 'src="../images/')
# If there are any other relative links in the template, fix them too
# For example, if there is a favicon link:
template = template.replace('href="images/', 'href="../images/')


projects = [
    {
        'filename': 'gamenexa',
        'title': 'GameNexa',
        'image': 'images/gamenexa.png',
        'description': 'A revolutionary web-based gaming platform that turns your smartphone into a gamepad.',
        'long_description': 'GameNexa redefines browser gaming by bridging the gap between mobile and desktop experiences. It transforms your smartphone into a fully functional, low-latency gamepad for playing high-quality 3D games on your desktop browser. Powered by WebRTC technology, it ensures real-time responsiveness without the need for expensive hardware or complex installations. Whether you are playing solo or with friends, GameNexa offers a seamless, console-like experience directly in your web browser.',
        'features': [
            'Smartphone as Controller: Turn any mobile device into a gamepad with zero-latency input.',
            'Instant Play: No downloads or installations required; play directly in the browser.',
            'Multiplayer Ecosystem: seamless local and online multiplayer support.',
            'Cross-Device Compatibility: Works on any device with a modern web browser.',
            'Real-Time WebRTC: Powered by cutting-edge WebRTC for instant connectivity.',
            '3D Browser Games: Optimized for high-fidelity 3D gaming experiences.'
        ],
        'tech': ['Next.js', 'WebRTC', 'Firebase', 'Phaser.js', 'Node.js', 'Socket.io', 'Tailwind CSS'],
        'links': [
            {'label': 'Live Demo', 'url': 'https://gamenexa.vercel.app/', 'icon': 'fas fa-external-link-alt'}
        ],
        'img_styles': 'object-position: top;'
    },
    {
        'filename': 'convertstream',
        'title': 'ConvertStream',
        'image': 'images/convertstream.png',
        'description': 'The world\'s most efficient cloud-based suite for file conversion and optimization.',
        'long_description': 'ConvertStream is a comprehensive, all-in-one cloud platform designed to streamline your file management workflow. It offers a robust suite of tools to convert, merge, split, and optimize files securely. From simple format conversions like Word to PDF to advanced AI-powered document summarization, ConvertStream handles it all with a user-friendly drag-and-drop interface. It leverages powerful cloud APIs to ensure high-quality processing without compromising your device\'s performance.',
        'features': [
            'PDF Tools: Merge, Split, Compress, Rotate, and Watermark PDFs easily.',
            'Format Conversion: Convert Word, Excel, PowerPoint, and Images to and from PDF.',
            'AI PDF Summarizer: Instantly generate concise summaries of long documents using AI.',
            'Security First: Files are processed securely and automatically deleted after use.',
            'Drag & Drop Interface: Intuitive and modern UI for seamless user experience.',
            'Cloud Processing: High-speed server-side processing for all operations.'
        ],
        'tech': ['Next.js', 'React', 'Tailwind CSS', 'Cloud APIs', 'Vercel', 'Python (Backend)', 'AI Integration'],
        'links': [
            {'label': 'Live Demo', 'url': 'https://convertstream.vercel.app/', 'icon': 'fas fa-external-link-alt'}
        ],
        'img_styles': 'object-position: top;'
    },
    {
        'filename': 'vtucrack',
        'title': 'VTUCRACK Education Portal',
        'image': 'images/vty.png',
        'description': 'Complete academic resource hub for VTU engineering students.',
        'long_description': 'VTUCRACK is a dedicated educational platform tailored specifically for students of Visvesvaraya Technological University (VTU). It acts as a comprehensive digital library, providing instant access to essential academic resources. From subject-wise notes and detailed lab manuals to previous years\' model question papers and real-time result updates, VTUCRACK simplifies the academic journey for engineering students across branches like CSE, ECE, ISE, Civil, and Mechanical.',
        'features': [
            'Comprehensive Notes: Subject-wise study materials for all semesters and branches.',
            'Lab Manuals: Detailed procedures, code snippets, and viva questions.',
            'Question Bank: Extensive archive of previous years\' model question papers.',
            'Instant Results: Quick and reliable access to VTU exam results and alerts.',
            'Syllabus & Updates: Up-to-date syllabus copies and university notifications.',
            'Student Community: A platform for sharing resources and peer learning.'
        ],
        'tech': ['PHP', 'MySQL', 'JavaScript', 'Bootstrap', 'HTML5/CSS3', 'jQuery'],
        'links': [
            {'label': 'Website', 'url': 'https://www.vtucrack.com/', 'icon': 'fas fa-external-link-alt'}
        ]
    },
    {
        'filename': 'iris-assistant',
        'title': 'IRIS AI Assistant',
        'image': 'images/jarvis.png',
        'description': 'Advanced AI-powered virtual assistant with voice recognition and system automation.',
        'long_description': 'IRIS (Intelligent Responsive Interactive System) is a sophisticated desktop assistant that brings the power of AI to your daily computing. Inspired by JARVIS, it combines advanced voice recognition, biometric security, and system control into a single interface. IRIS leverages multiple AI models like Groq and Gemini for intelligent conversations and supports complex automation tasks, making it a true personal assistant for your desktop.',
        'features': [
            'Biometric Security: Face recognition and fingerprint authentication for secure access.',
            'Multi-AI Integration: Powered by Groq and Google Gemini for smart responses.',
            'Voice Command & Control: Real-time speech recognition and text-to-speech synthesis.',
            'System Automation: Open apps, manage files, and control system settings via voice.',
            'Mobile Integration: Control your PC remotely using the Android companion app with ADB.',
            'Smart Features: Emotion detection, proactive suggestions, and learning capabilities.'
        ],
        'tech': ['Python', 'OpenCV', 'TensorFlow', 'Tkinter', 'OpenAI API/Groq', 'PyAutoGUI', 'SpeechRecognition'],
        'links': [
            {'label': 'Live Demo', 'url': 'https://iris-ai-assistant-yjnq.vercel.app/', 'icon': 'fas fa-external-link-alt'},
            {'label': 'View Code', 'url': 'https://github.com/Avinashb722/jarvis-ai-assistant', 'icon': 'fab fa-github', 'class': 'secondary'}
        ]
    },
    {
        'filename': 'suraksha-safety',
        'title': 'Suraksha Safety Platform',
        'image': 'images/suraksha.png',
        'description': 'Real-time women safety application with emergency SOS and tracking.',
        'long_description': 'Suraksha is an advanced women safety web application designed to provide immediate assistance in critical situations. It features a robust one-tap SOS system that instantly broadcasts distress signals and real-time location data to trusted contacts and emergency services. Built with a focus on speed and reliability, Suraksha ensures that help is always just a click away, even in low-bandwidth environments.',
        'features': [
            'One-Tap SOS: Instantly send distress signals via SMS and Email.',
            'Live GPS Tracking: Real-time location sharing with Google Maps integration.',
            'Voice Activation: Hands-free SOS triggering using voice commands.',
            'Incident Reporting: Securely document and report safety incidents with evidence.',
            'Multi-Channel Alerts: Simultaneous notifications via SMS, Email, and Push.',
            'Trusted Contacts: Manage emergency contacts with priority levels.'
        ],
        'tech': ['React.js', 'Node.js', 'MongoDB', 'Express.js', 'Google Maps API', 'Twilio/Fast2SMS', 'Socket.io'],
        'links': [
            {'label': 'View Code', 'url': 'https://github.com/Avinashb722/suraksha-women-safety-web', 'icon': 'fab fa-github'}
        ]
    },
    {
        'filename': 'chatgpt-clone',
        'title': 'AI ChatGPT Clone',
        'image': 'images/chat clone.png',
        'description': 'Feature-rich multi-model AI chat system with document analysis and code execution.',
        'long_description': 'This project is a powerful clone of ChatGPT that extends functionality beyond standard text generation. It supports multiple AI backends including GPT-4, Gemini, and local LLMs via GPT4All. Users can upload documents for analysis, generate PDFs and PowerPoints from prompts, and even execute code in a secure sandbox. It offers a modern, responsive chat interface with a built-in API layer for external integration.',
        'features': [
            'Multi-Model AI: Switch between Groq (Llama 3), Google Gemini, and Local GPT4All models.',
            'Document Analysis: Chat with uploaded PDFs, DOCX files, and images (OCR included).',
            'Content Generation: Auto-generate PDFs, PowerPoint slides, and Word docs from text.',
            'Code Sandbox: Securely execute Python, JavaScript, C++, and Java code.',
            'Voice Interface: Integrated speech-to-text and text-to-speech with multiple voices.',
            'API Access: Ready-made API endpoints for integrating AI into other apps.'
        ],
        'tech': ['Flask', 'Python', 'JavaScript', 'LangChain', 'OpenAI API', 'ChromaDB'],
        'links': [
            {'label': 'View Code', 'url': 'https://github.com/Avinashb722/chatgpt_clone', 'icon': 'fab fa-github'}
        ]
    },
    {
        'filename': 'mobile-jarvis',
        'title': 'Mobile Jarvis Assistant',
        'image': 'images/mobile jarvis.jpg',
        'description': 'Advanced mobile AI assistant for remote desktop control.',
        'long_description': 'Mobile Jarvis bridges the gap between your smartphone and personal computer. It serves as a portable command center, allowing you to control your desktop environment remotely, execute system commands, and access files from anywhere. Optimized for Android, it features a native voice interface and secure encrypted connection.',
        'features': [
            'Remote Desktop Control: Execute commands and launch apps from your phone.',
            'Voice Integration: Control your PC using natural voice commands.',
            'File Management: Browse and access PC files remotely.',
            'System Monitoring: View real-time system stats on your mobile.',
            'Secure Connection: Encrypted data transmission for privacy.'
        ],
        'tech': ['Android (Java)', 'Python', 'Socket Programming', 'Firebase'],
        'links': [
            {'label': 'View Code', 'url': 'https://github.com/Avinashb722/jarvis-ai-assistant', 'icon': 'fab fa-github'}
        ]
    },
    {
        'filename': 'line-robot',
        'title': 'Autonomous Line Robot',
        'image': 'images/line folling.jpg',
        'description': 'Intelligent robotic system with advanced path tracking algorithms.',
        'long_description': 'This project is an autonomous robot designed to navigate complex paths using infrared sensors. It implements a PID control algorithm for smooth line following and integrates ultrasonic sensors for real-time obstacle detection and avoidance. It showcases the integration of hardware (sensors, motors) with embedded software logic.',
        'features': [
            'Precision Navigation: PID-controlled line following logic.',
            'Obstacle Avoidance: Ultrasonic detection and automatic rerouting.',
            'Sensor Fusion: Combines IR and Ultrasonic data for decision making.',
            'Modular Design: easily expandable hardware architecture.',
            'Embedded Logic: Efficient C++ code optimized for Arduino.'
        ],
        'tech': ['Arduino', 'C++', 'Eagle CAD', 'Sensors (IR/Ultrasonic)', 'Embedded Systems'],
        'links': [
            {'label': 'View Code', 'url': 'https://github.com/Avinashb722/line-following-robot', 'icon': 'fab fa-github'}
        ]
    }
]

for project in projects:
    tech_tags_html = ''.join([f'<span class="tech-tag" style="background: var(--gray-100); color: var(--gray-700); padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.875rem; font-weight: 500; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">{tag}</span>' for tag in project['tech']])
    
    features_html = '<ul style="list-style-type: none; padding: 0;">'
    for feature in project.get('features', []):
        features_html += f'<li style="margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative;"><i class="fas fa-check-circle" style="color: var(--primary); position: absolute; left: 0; top: 4px;"></i> {feature}</li>'
    features_html += '</ul>'

    links_html = ''
    for link in project['links']:
        btn_class = 'btn-primary' if link.get('class') != 'secondary' else 'btn-outline'
        links_html += f'''
        <a href="{link['url']}" class="btn {btn_class}" target="_blank">
            <i class="{link['icon']}"></i>
            {link['label']}
        </a>
        '''
    
    img_style = project.get('img_styles', '')
    
    project_slug = project['filename'].replace('.html', '')
    
    content = f'''
    <section class="section" style="padding-top: 120px;">
        <div class="container">
            <div class="section-header" style="text-align: left; margin-bottom: 2rem;">
                <a href="../index.html#projects" class="btn btn-outline" style="margin-bottom: 2rem;"><i class="fas fa-arrow-left"></i> Back to Portfolio</a>
                <h1 class="section-title" style="font-size: 3rem;">{project['title']}</h1>
            </div>
            
            <div class="project-details" style="background: white; border-radius: 1rem; padding: 2rem; box-shadow: var(--shadow);">
                <div class="project-hero-image" style="margin-bottom: 2rem; border-radius: 0.5rem; overflow: hidden; height: 500px;">
                    <img src="../{project['image']}" alt="{project['title']}" style="width: 100%; height: 100%; object-fit: cover; {img_style}">
                </div>
                
                <div class="project-grid" style="display: grid; grid-template-columns: 2fr 1fr; gap: 3rem;">
                    <div class="project-main">
                        <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--gray-900); margin-bottom: 1rem;">About the Project</h3>
                        <p style="color: var(--gray-600); margin-bottom: 2rem; line-height: 1.8; font-size: 1.1rem;">{project.get('long_description', project['description'])}</p>
                        
                        <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--gray-900); margin-bottom: 1rem;">Key Features</h3>
                        <div class="project-features" style="margin-bottom: 2rem;">
                            {features_html}
                        </div>
                    </div>
                    
                    <div class="project-sidebar">
                        <div class="sidebar-widget" style="background: var(--gray-50); padding: 1.5rem; border-radius: 1rem; margin-bottom: 2rem;">
                            <h4 style="font-size: 1.25rem; font-weight: 700; color: var(--gray-900); margin-bottom: 1rem;">Technologies</h4>
                            <div class="project-tech">
                                {tech_tags_html} 
                            </div>
                        </div>
                        
                        <div class="sidebar-widget" style="background: var(--gray-50); padding: 1.5rem; border-radius: 1rem;">
                            <h4 style="font-size: 1.25rem; font-weight: 700; color: var(--gray-900); margin-bottom: 1rem;">Links</h4>
                            <div class="project-actions" style="display: flex; flex-direction: column; gap: 1rem;">
                                {links_html}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
        @media (max-width: 992px) {{
            .project-grid {{
                grid-template-columns: 1fr !important;
            }}
        }}
    </style>
    '''
    
    new_page = template.replace('<!-- PROJECT_CONTENT -->', content)
    
    # Create directory for Clean URL support
    if not os.path.exists(project_slug):
        os.makedirs(project_slug)
        
    file_path = os.path.join(project_slug, 'index.html')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_page)
    print(f"Created {file_path}")
