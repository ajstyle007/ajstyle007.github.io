import streamlit as st
import base64

st.set_page_config(
    page_title="Ajay's Portfolio",  # ✅ This sets the tab title
    page_icon="sm.png",                 # (Optional) Sets the favicon
    layout="centered"                   # (Optional) Use 'centered' or 'wide'
)

st.markdown(
    """<div style="font-size: 40px; line-height: 1; margin-bottom: -10px; font-weight: bold; font-style: normal; font-family:Arial; color: #43443e;">
        Ajay Kumar
          </div>"""
          ,unsafe_allow_html=True,)
# st.subheader("A Data Science Enthusiast")
st.markdown(
    """<div style="font-size: 25px; margin-bottom: 20px; font-style: normal; font-family:calibri; color: #645b59;">
        A Data Science Enthusiast
          </div>"""
          ,unsafe_allow_html=True,)

col1, col2 = st.columns([3,2])

with col1:

    st.markdown(
    """<div style="font-size: 18px; font-style: normal; font-family:calibri; color: #676160;">
        Passionate Data Science professional with more than 1 year of hands-on experience in building AI, ML, 
        and Data Science solutions. Over this journey, I’ve worked on diverse projects ranging 
        from AI-powered stock market assistants and medical chatbots to computer vision, NLP, 
        and predictive modeling applications. My expertise spans across data preprocessing, 
        model development, deployment, and MLOps practices, with a focus on applying advanced 
        techniques like Retrieval-Augmented Generation (RAG), Generative AI, and Deep Learning architectures.
          </div>"""
          ,unsafe_allow_html=True,) 
    st.markdown("")
             
    st.markdown(
    """<div style="font-size: 18px; font-style: normal; font-family: calibri; color: #676160;">
        Beyond projects, I share my learnings through blogs on Medium, covering topics like linear regression 
        for interviews, spam classification, recommendation systems, and AI-powered stock market chatbots.
        I’m passionate about bridging research and real-world applications, 
        continuously learning, and building impactful AI-driven solutions that solve meaningful problems.
          </div>"""
          ,unsafe_allow_html=True,)

# Function to encode the image as Base64
def get_base64_image(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")   
with col2:

    image_path = "photo.png"

    st.markdown(
    """
    <style>
    .custom-img {
        border-radius: 10px; width: 260px; height: 290px;
    }
    </style>""",unsafe_allow_html=True,)

    image_base64 = get_base64_image(image_path)

    st.markdown(
    f"""<img src="data:image/png;base64,{image_base64}" class="custom-img">""",unsafe_allow_html=True,)


    
    # email code
    st.markdown(
    """
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    """,
    unsafe_allow_html=True)

    # Display the email envelope icon with the email address
    # email code
    st.markdown(
        """
        <p style="font-size: 15px; margin-bottom: -10px; margin-left: 25px;">
        <a href="mailto:kumarajaypaonta@gmail.com">
            <i class="fa fa-envelope" style="font-size: 15px; color: #464443;"></i>
        </a>&nbsp;
            <a href="mailto:kumarajaypaonta@gmail.com" style="text-decoration: none; color: #413e3d;">kumarajaypaonta@gmail.com</a>
        </p>
        """,
        unsafe_allow_html=True)

    # Display the clickable GitHub icon with the GitHub link
    # github code
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007" target="_blank" style="text-decoration: none; color: #413e3d;">@ajstyle007</a>
        </p>
        """,
        unsafe_allow_html=True)

    # linkedin code
    st.markdown(
    """
    <p style="font-size: 15px; line-height: 1.6; margin-left: 25px; margin-bottom: -10px;">
        <a href="https://www.linkedin.com/in/ajay-kumar-72ba861b8/" target="_blank">
            <i class="fab fa-linkedin" style="font-size: 15px; color: #0e76a8;"></i>
        </a>&nbsp;
        <a href="https://www.linkedin.com/in/ajay-kumar-72ba861b8/" target="_blank" style="text-decoration: none; color: #413e3d;">@LinkedIn</a>
    </p>
    """,
    unsafe_allow_html=True)

    # hugging face
    st.markdown(
    """
    <p style="font-size: 15px; line-height: 1.6; margin-left: 25px; margin-bottom: -10px;">
        <a href="https://huggingface.co/musk12" target="_blank">
            <i class="fas fa-smile" style="font-size: 15px; color: #d3bf16;"></i>
        </a>&nbsp;
        <a href="https://huggingface.co/musk12" target="_blank" style="text-decoration: none; color: #413e3d;">@Hugging Face</a>
    </p>
    """,
    unsafe_allow_html=True)

    # medium
    st.markdown(
    """
    <p style="font-size: 15px; line-height: 1.6; margin-left: 25px;">
        <a href="https://medium.com/@kumarajaypaonta" target="_blank">
            <i class="fa-brands fa-monero" style="font-size: 15px; color: #464443;"></i>
        </a>&nbsp;
        <a href="https://medium.com/@kumarajaypaonta" target="_blank" style="text-decoration: none; color: #413e3d;">@Medium Blogs</a>
    </p>
    """,
    unsafe_allow_html=True)

    # resume code
    # st.markdown(
    # """
    # <p style="font-size: 25px; line-height: 1; margin-left: 20px; border: 2px solid #464443; padding: 10px; border-radius: 5px; display: inline-block;">
    #     <!-- Resume Emoji with name as clickable -->
    #     <a href="https://drive.google.com/file/d/1AC2oWwurifxmgK6hn1OcJf4YVGkXEUyZ/view?usp=sharing" target="_blank" style="text-decoration: none; color: #464443;">
    #         <span style="font-size: 25px;">📝</span> 
    #         <span style="margin-left: 10px;">Resume</span>
    #     </a>
    # </p>
    # """,
    # unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 10px;">
        <button style="background-color: #333; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; margin-right: 60px;">
            <a href="https://drive.google.com/file/d/1CV4KKP_bfnwi9CeTL7PEIIu8oOiAAs2Z/view?usp=sharing" download style="color: #fff; text-decoration: none;">Resume <i class="fas fa-download"></i></a>
        </button>
    </div>
    """, unsafe_allow_html=True,)





st.markdown("""
<style>
/* Container for the personal info box */
.personal-info-container {
    background-color: #1e1e1e; /* Dark background */
    color: #ffffff; /* White text */
    border: 2px solid #444;   /* Border color */
    border-radius: 10px;      /* Rounded corners */
    padding: 20px;            /* Inner padding */
    margin: 20px 0;           /* Space outside the box */
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5); /* Add shadow for a modern look */
}

/* Title for the personal info box */
.personal-info-title {
    font-family: "Courier New", Courier, monospace;
    font-size: 24px;
    font-weight: bold;
    color: #9ca090; /* Gold color for the title */
    text-align: center;
    margin-bottom: 20px;
}

/* Info rows styling */
.personal-info-row {
    font-family: "Courier New", Courier, monospace;
    font-size: 15px;
    margin: 10px 0; /* Space between rows */
    line-height: 1.5; /* Line spacing */
}

/* Highlight labels in rows */
.personal-info-row span {
    font-weight: bold;
    color: #60625c; /* Green for labels */
}
</style>
""", unsafe_allow_html=True)

# Personal info box content
st.markdown("""
<div class="personal-info-container">
    <div class="personal-info-title">About Me</div>
    <div class="personal-info-row"><span>Name:</span> Ajay Kumar</div>
    <div class="personal-info-row"><span>Education:</span> B.Tech. in Electronics and communication</div>
    <div class="personal-info-row"><span>University:</span> Himachal Pradesh Technical University</div>
    <div class="personal-info-row"><span>Current Address:</span> Mohali Punjab, India</div>
    <div class="personal-info-row"><span>Phone:</span> 7876757653</div>
    <div class="personal-info-row"><span>Email:</span> kumarajaypaonta@gmail.com</div>
</div>
""", unsafe_allow_html=True)



# skills section

# projects sections
st.write("")
st.markdown("---")
st.write("")
st.markdown(
    """<div style="font-size: 35px; line-height: 1; margin-bottom: -10px; font-weight: bold; font-style: normal; font-family:Arial; color: #5a5f61;">
        Skills
          </div>"""
          ,unsafe_allow_html=True,)

st.write("")
st.write("")

st.markdown("""
<style>
/* Outer container (box for all skills) */
.skills-container {
    background-color: #1e1e1e; /* Dark background */
    border: 2px solid #444;   /* Border around the box */
    border-radius: 10px;      /* Rounded corners */
    padding: 20px;            /* Space inside the box */
    margin: 10px 0;           /* Space outside the box */
}

/* Skills section container */
.skills-section {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
}

/* Individual skill box */
.skill-box {
    font-family: Arial, sans-serif;
    font-size: 12px;
    font-weight: bold;
    color: Black;
    padding: 7px 15px;
    border-radius: 4px;
    text-align: center;
    display: inline-block;
}

.skills-title {
    font-family: Arial, sans-serif;
    font-size: 15px;
    font-weight :bold;
    color: #9ca090; /* Change this to your desired color */
    margin-bottom: 20px;
    text-align: center;
}

/* Define colors for each skill */
.python { background-color: #74776d; }        /* Python Blue */
.git { background-color: #74776d; }          /* Git Orange */
.vscode { background-color: #74776d; }       /* VS Code Blue */
.jupyter { background-color: #74776d; }      /* Jupyter Orange */
.colab { background-color: #74776d; }        /* Colab Yellow */
.tensorflow { background-color: #74776d; }   /* TensorFlow Orange */
.pytorch { background-color: #74776d; }      /* PyTorch Red */
.ml { background-color: #74776d; }           /* Machine Learning Green */
.ds { background-color: #74776d; }           /* Data Science Blue */
.dl { background-color: #74776d; }           /* Deep Learning Orange */
.nlp { background-color: #74776d; }          /* NLP Purple */
.sklearn { background-color: #74776d; }      /* Scikit-learn Yellow */
.nn { background-color: #74776d; }           /* Neural Networks Pink */
.streamlit { background-color: #74776d; }    /* Streamlit Red */
.html { background-color: #74776d; }         /* HTML5 Red */
.css { background-color: #74776d; }          /* CSS3 Blue */
.huggingface { background-color: #74776d; }  /* Hugging Face Yellow */
.MLOPS {background-color: #74776d;}          /* MLOPS Purple */
.dvc {background-color: #74776d;}            /* dvc pink */
.mlflow {background-color: #74776d;}         /* mlfow green */
.GenAI {background-color: #74776d;}          /* GenAI */  
.LLMs {background-color: #74776d;}           /* LLMs */
.RAG {background-color: #74776d;}            /* RAG */ 
.Web_Scraping {background-color: #74776d;}   /* Web Scraping */
.FAST_API {background-color: #74776d;}       /* FAST_API*/
.GANs {background-color: #74776d;}           /* GANs */
.Transformers {background-color: #74776d;}   /* Transformers */

</style>
""", unsafe_allow_html=True)

# Render the skills section
st.markdown("""
<div class="skills-container">
    <div class="skills-title">Tools and Skills I use.</div>
    <div class="skills-section">
        <div class="skill-box python">Python</div>
        <div class="skill-box git">Git</div>
        <div class="skill-box vscode">VS Code</div>
        <div class="skill-box jupyter">Jupyter Notebook</div>
        <div class="skill-box colab">Google Colab</div>
        <div class="skill-box tensorflow">TensorFlow</div>
        <div class="skill-box pytorch">PyTorch</div>
        <div class="skill-box ml">Machine Learning</div>
        <div class="skill-box ds">Data Science</div>
        <div class="skill-box dl">Deep Learning</div>
        <div class="skill-box nlp">NLP</div>
        <div class="skill-box sklearn">Scikit-learn</div>
        <div class="skill-box nn">Neural Networks</div>
        <div class="skill-box streamlit">Streamlit</div>
        <div class="skill-box html">HTML5</div>
        <div class="skill-box css">CSS3</div>
        <div class="skill-box huggingface">Hugging Face Spaces</div>
        <div class="skill-box MLOPS">MLOPS</div>
        <div class="skill-box dvc">dvc</div>
        <div class="skill-box mlflow">mlflow</div>
        <div class="skill-box GenAI">GEN AI</div>
        <div class="skill-box LLMs">LLMs</div>
        <div class="skill-box RAG">RAG</div>
        <div class="skill-box Web_Scraping">Web Scraping</div>
        <div class="skill-box FAST_API">FAST API</div>
        <div class="skill-box GANs">GANs</div>
        <div class="skill-box Transformers">Transformers</div>
    </div>
    </div>
</div>
""", unsafe_allow_html=True)
           

# projects sections
st.write("")
st.write("")
st.write("")
st.markdown(
    """<div style="font-size: 35px; line-height: 1; margin-bottom: -10px; font-weight: bold; font-style: normal; font-family:Arial; color: #5a5f61;">
        Projects
          </div>"""
          ,unsafe_allow_html=True,)

st.write("")
st.write("")


# url = "https://www.appier.com/hubfs/Imported_Blog_Media/GettyImages-1030850238-01.jpg"
# first project

# st.markdown(
#     """
    
#     <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px; margin: 20px 0;">
#         <h3 style="margin: 0;">Project Title: Movie Gen</h3>
#         <p style="margin: 5px 0;">By: The Movie Gen Team</p>
#         <a href="https://example.com/live-app" target="_blank" style="text-decoration: none; color: blue;">Live App</a>
#         <br>
#         <a href="https://example.com/blog" target="_blank" style="text-decoration: none; color: blue;">Blog</a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


# -7 project
st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://github.com/ajstyle007/Transformer-Encoder-from-scratch-using-Pytorch/blob/main/encoder2.png?raw=true", caption=None, width=120)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_deeplearning-encoder-transformers-activity-7398066672323977216-5R0i?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_deeplearning-encoder-transformers-activity-7398066672323977216-5R0i?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank" style="text-decoration: none; color: #43443e;">LinkedIn</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/Transformer-Encoder-from-scratch-using-Pytorch/" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/Transformer-Encoder-from-scratch-using-Pytorch/" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-transformer-encoder-demo.hf.space/" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-transformer-encoder-demo.hf.space/" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### Implementing the Transformer Encoder from scratch using PyTorch.
        Implementing the Transformer Encoder from scratch using PyTorch — exactly as described in “Attention is All You Need” 
        and also implements Multi-Head Attention, Positional Encoding, Feed-Forward networks, Residual+LayerNorm, 
        and an encoder stack from first principles. The encoder was trained on KP20k (BIO labels) to validate 
        the implementation and to experiment with attention behavior, head effects and extraction heuristics.*

        ***#DeepLearning #Encoder #Transformers #NLP #AttentionIsAllYouNeed #PyTorch #MachineLearning #AI #ArtificialIntelligence***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)




# -6 project
st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*YuYhnVyxRiid6EJwTbsUDg.png", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_computervision-deeplearning-pytorch-activity-7384682216657887233-msQn?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_computervision-deeplearning-pytorch-activity-7384682216657887233-msQn?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank" style="text-decoration: none; color: #43443e;">LinkedIn</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/YOLOv1-Paper-Implementation-using-PyTorch-from-scratch" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/YOLOv1-Paper-Implementation-using-PyTorch-from-scratch" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-yolov1-detection.hf.space/" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-yolov1-detection.hf.space/" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### YOLOv1-Research Paper-Implementation-using-PyTorch-from-scratch.
        *This project is a from-scratch implementation of the YOLOv1 (You Only Look Once) 
        object detection paper using PyTorch. I implemented the entire pipeline — architecture, 
        loss function, dataset parsing, and model training — to deeply understand how YOLO works at its core.*

        ***#YOLOv1 #ComputerVision #DeepLearning #PyTorch #ObjectDetection #AIResearch #HuggingFace #AIProject #DeepLearningProject***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)





# -5 project
st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://media.springernature.com/lw1200/springer-static/image/art%3A10.1007%2Fs44163-024-00138-z/MediaObjects/44163_2024_138_Fig5_HTML.png", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_gan-dcgan-deeplearning-activity-7375884130598752256-tRCs?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_gan-dcgan-deeplearning-activity-7375884130598752256-tRCs?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank" style="text-decoration: none; color: #43443e;">LinkedIn</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/GAN-Research-Paper-Implementation" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/GAN-Research-Paper-Implementation" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-face-generation-and-morphing-application.hf.space/" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-face-generation-and-morphing-application.hf.space/" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### Implementation of GAN Research Papers: From Concept to Face Generation.
        *Implemented and trained a DCGAN model to generate realistic human faces using the CelebA dataset. 
        Built an interactive web interface with Flask, HTML, CSS, and JavaScript that allows users to generate faces, 
        morph between two faces with a slider, and create batches of 100 synthetic faces. 
        Deployed the project on Hugging Face Spaces, showcasing end-to-end GAN implementation from research paper to real-time user interaction.*

        ***#GAN #DCGAN #DeepLearning #ComputerVision #FaceGeneration #PyTorch #AIResearch #HuggingFace #ImageGeneration #AIProject #DeepLearningProject***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)







# -4 project
st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://lh3.googleusercontent.com/hH2WyFtw00oaE97RlW8Wj5ZlR_e0xt2T3-yNgYxYjjQlsFtj4GrXfIOgdm6RYLyLJ1PZTJAg1Abdd-QWxHC_tnQ2=s1280-w1280-h800", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_ai-langchain-fastapi-activity-7370810672701456384-eYPC?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://www.linkedin.com/posts/ajay-kumar1998_ai-langchain-fastapi-activity-7370810672701456384-eYPC?utm_source=share&utm_medium=member_desktop&rcm=ACoAADK0bJMBz8diuWhp9-h6Y2JjrHRA10bjVOQ" target="_blank" style="text-decoration: none; color: #43443e;">LinkedIn</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/stock-chat-Bot-extension" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/stock-chat-Bot-extension" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://medium.com/@kumarajaypaonta/behind-the-code-building-a-stock-market-chatbot-with-fastapi-selenium-and-langchain-b21e5dc88c6b" target="_blank">
                <i class="fa-solid fa-file-contract" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://medium.com/@kumarajaypaonta/behind-the-code-building-a-stock-market-chatbot-with-fastapi-selenium-and-langchain-b21e5dc88c6b" target="_blank" style="text-decoration: none; color: #43443e;">Blog</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### AI-Powered Stock Market Insights: Building a Chrome Extension with Selenium, FastAPI, and LangChain.
        *I built a Chrome extension powered by Selenium, FastAPI, and LangChain that works as an 
        AI-driven stock market chatbot assistant. With a simple natural language query, 
        it can fetch real-time stock performance, show detailed stats for any stock, provide sector-wise
        insights, pull the latest market news, and display interactive charts — all directly inside the 
        browser.*

        ***#AI #ChromeExtension #StockMarket #LangChain #FastAPI #Selenium #AIChatbot #MarketInsights #Automation***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)






# -3 project
st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://github.com/ajstyle007/U-Net-Paper-Implementation-Car-Segmentation-/blob/main/unet_arch.jpg?raw=true", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-car-segmentation-mask.hf.space/" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-car-segmentation-mask.hf.space/" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/U-Net-Paper-Implementation-Car-Segmentation-/tree/main" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/U-Net-Paper-Implementation-Car-Segmentation-/tree/main" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://arxiv.org/pdf/1505.04597" target="_blank">
                <i class="fas fa-file-alt" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://arxiv.org/pdf/1505.04597" target="_blank" style="text-decoration: none; color: #43443e;">Research Paper</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### Implementation of U-Net Research Paper using PyTorch for Car Image Segmentation and Mask Generation.
        *I have implemented the original U-Net research paper using PyTorch and then trained this model on a car dataset.
        created the frontend to use this model and generate the mask of the car. For the frontend, 
        I used Flask, HTML, and CSS. In the app, I can upload an image, and by clicking a button, 
        it generates the mask and overlay of the original image.*

        ***#DeepLearning #PyTorch #UNet #ImageSegmentation #Flask #DataScience #AI #MaskGeneration #ProjectLearning***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)






# -2 project
st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://austincareerinstitute.edu/wp-content/uploads/2023/12/ma-ai-scaled.jpg", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-rag-medical-bot.hf.space" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-rag-medical-bot.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/Rag-Medical-Assistant/tree/main" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/Rag-Medical-Assistant/tree/main" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### An AI-powered medical assistant leveraging WHO data via RAG.
        *An AI-powered medical assistant leveraging Retrieval-Augmented Generation (RAG) on WHO data to 
        deliver accurate medical responses. Built with a modular Flask (frontend) and FastAPI (backend) 
        architecture, integrated with Pinecone for semantic search, MongoDB for patient data, and containerized
        with Docker for seamless deployment on Hugging Face Spaces.*

        ***#AI #RAG #MedicalAI #Healthcare #WHO #FastAPI #Flask #Docker #Pinecone #MongoDB #LLM #MachineLearning #HuggingFaceSpaces***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)






# -1 project

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://miro.medium.com/v2/resize:fit:1200/1*biZq-ihFzq1I6Ssjz7UtdA.jpeg", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-dog-cat-classifier-with-resnet-50.hf.space" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-dog-cat-classifier-with-resnet-50.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/dog_vs_cat-using-pretrained-model--resnet50-/tree/master" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/dog_vs_cat-using-pretrained-model--resnet50-/tree/master" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### Dog Cat Classifier using pretrained model Resnet50
        *This project is deep learning-based image classification model that distinguishes between dogs and cats 
        using the ResNet50 architecture. The model leverages transfer learning from a pretrained 
        ResNet50 network (trained on ImageNet) to achieve high accuracy (95.36%) 
        with minimal training time.*

        ***#DeepLearning #resnet50 #transferlearning #dogvscatclassifier***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)



# zero project

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

# Content in the first column
with col1:
    st.image("https://i.ytimg.com/vi/kP6nWbJqIbo/maxresdefault.jpg", caption=None, use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://musk12-rainfall-prediction-with-mlflow.hf.space" target="_blank">
                <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://musk12-rainfall-prediction-with-mlflow.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
        </p>
        """,
        unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://github.com/ajstyle007/Rainfall-prediction-with-mlflow/tree/main" target="_blank">
                <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
            </a>&nbsp;
            <a href="https://github.com/ajstyle007/Rainfall-prediction-with-mlflow/tree/main" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
        </p>
        """,
        unsafe_allow_html=True)

# Content in the second column
with col2:
    st.markdown(
        """
        ### RainFall Prediction using ML and Experiment tracking with MLflow
        *This project focuses on predicting rainfall using machine learning techniques while implementing 
        experiment tracking with MLflow and DagsHub. The goal is to build an accurate model that 
        forecasts rainfall based on meteorological features.*

        ***#MachineLearning #mlflow #mlops #RainFallprediction***
        """
    )

st.markdown(
    """
    <hr style="border: none; height: 0.5px; background-color: #333;" />
    """,unsafe_allow_html=True)








# if "show_more_projects" not in st.session_state:
#     st.session_state.show_more_projects = False

# def toggle_projects():
#     st.session_state.show_more_projects = not st.session_state.show_more_projects

# if st.button("More Projects", on_click=toggle_projects):
#     pass




# if st.session_state.show_more_projects:
with st.expander("▼ More Projects", expanded=False):


    # second project

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    # Content in the first column
    with col1:
        st.image("https://www.financialexpress.com/wp-content/uploads/2023/12/gmail-logo-header-resized.jpg?w=350", caption=None, use_container_width=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://musk12-email-spam-classifier.hf.space" target="_blank">
                    <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://musk12-email-spam-classifier.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://medium.com/@kumarajaypaonta/fighting-spam-with-machine-learning-building-an-effective-email-and-sms-classifier-96a5a201a954" target="_blank">
                    <i class="fa-solid fa-file-contract" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://medium.com/@kumarajaypaonta/fighting-spam-with-machine-learning-building-an-effective-email-and-sms-classifier-96a5a201a954" target="_blank" style="text-decoration: none; color: #43443e;">Blog</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://github.com/ajstyle007/Email-SMS-Spam-classifier" target="_blank">
                    <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://github.com/ajstyle007/Email-SMS-Spam-classifier" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
            </p>
            """,
            unsafe_allow_html=True)

    # Content in the second column
    with col2:
        st.markdown(
            """
            ### Email Spam Classifier
            *This project focuses on developing a robust Email/SMS Spam Classifier that leverages machine learning techniques to 
            accurately distinguish between spam (unwanted) and ham (legitimate) messages.*

            ***#MachineLearning #NLP #DataScience #SpamDetection***
            """
        )

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)




    # first project
    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    # Content in the first column
    with col1:
        st.image("https://www.appier.com/hubfs/Imported_Blog_Media/GettyImages-1030850238-01.jpg", caption=None, use_container_width=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://musk12-cx-churn-prediction-with-pytorch.hf.space" target="_blank">
                    <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://musk12-cx-churn-prediction-with-pytorch.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://github.com/ajstyle007/Cx-Churn-Prediction-Model-Using-ANN-and-PyTorch-" target="_blank">
                    <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://github.com/ajstyle007/Cx-Churn-Prediction-Model-Using-ANN-and-PyTorch-" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
            </p>
            """,
            unsafe_allow_html=True)

    # Content in the second column
    with col2:
        st.markdown(
            """
            ### Cx Churn Prediction With PyTorch
            *This project predicts customer churn in credit card services using an Artificial Neural Network (ANN) built with PyTorch. 
            The model was trained on the Credit Card Customer Churn Prediction dataset from Kaggle, achieving an accuracy of 86%.*

            ***#DeepLearning #ArtificialNeuralNetwork #PyTorch #CustomerChurn***
            """
        )

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)



    # third project
    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    # Content in the first column
    with col1:
        st.image("https://cdn.slidesharecdn.com/ss_thumbnails/bookrecommendations-230615063942-3b1016c9-thumbnail.jpg?width=640&height=640&fit=bounds", caption=None, use_container_width=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://musk12-book-recommender-system.hf.space" target="_blank">
                    <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://musk12-book-recommender-system.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://medium.com/@kumarajaypaonta/from-data-to-recommendations-creating-a-machine-learning-book-recommender-system-18fe5950368b" target="_blank">
                    <i class="fa-solid fa-file-contract" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://medium.com/@kumarajaypaonta/from-data-to-recommendations-creating-a-machine-learning-book-recommender-system-18fe5950368b" target="_blank" style="text-decoration: none; color: #43443e;">Blog</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://github.com/ajstyle007/Book-Recommender-System" target="_blank">
                    <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://github.com/ajstyle007/Book-Recommender-System" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
            </p>
            """,
            unsafe_allow_html=True)

    # Content in the second column
    with col2:
        st.markdown(
            """
            ### Book Recommender System
            *In this project, I developed a Book Recommender System using a combination of popularity-based and collaborative filtering techniques. 
            The system helps users discover books based on their reading history and interactions with books, and it also highlights the top-rated books. 
            The model is deployed using a web application built with Streamlit and hosted on Hugging Face.*

            ***#RecommenderSystem #AI #MachineLearning #BookRecommendations #CollaborativeFiltering***
            """
        )

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)


    # fourth project

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    # Content in the first column
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvKIpGpyoXtl1gLI0y6K5NmBuZWZ5PbTL9TQ&s", caption=None, use_container_width=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://musk12-ipl-eda.hf.space" target="_blank">
                    <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://musk12-ipl-eda.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
            </p>
            """,
            unsafe_allow_html=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://medium.com/@kumarajaypaonta/exploratory-data-analysis-of-ipl-dataset-2008-2022-c38b78239e4f" target="_blank">
                    <i class="fa-solid fa-file-contract" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://medium.com/@kumarajaypaonta/exploratory-data-analysis-of-ipl-dataset-2008-2022-c38b78239e4f" target="_blank" style="text-decoration: none; color: #43443e;">Blog</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://github.com/ajstyle007/ipl-project" target="_blank">
                    <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://github.com/ajstyle007/ipl-project" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
            </p>
            """,
            unsafe_allow_html=True)

    # Content in the second column
    with col2:
        st.markdown(
            """
            ### Exploratory Data Analysis of IPL Dataset
            *I’ve developed a dynamic web application using Streamlit that offers insightful analysis of IPL data. 
            This user-friendly app allows enthusiasts to explore the vast IPL dataset interactively.*

            ***#DataAnalysis #IPL #Cricket #IPLEDA***
            """
        )

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)
    

    # fifth project

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    # Content in the first column
    with col1:
        st.image("https://assets.editorial.aetnd.com/uploads/2010/01/gettyimages-466313493-2.jpg", caption=None, use_container_width=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://musk12-olympic-eda.hf.space" target="_blank">
                    <i class="fa-solid fa-link" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://musk12-olympic-eda.hf.space" target="_blank" style="text-decoration: none; color: #43443e;">live link</a>
            </p>
            """,
            unsafe_allow_html=True)

        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://medium.com/@kumarajaypaonta/olympics-unveiled-an-in-depth-exploratory-data-analysis-d87f32596528" target="_blank">
                    <i class="fa-solid fa-file-contract" style="font-size: 20px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://medium.com/@kumarajaypaonta/olympics-unveiled-an-in-depth-exploratory-data-analysis-d87f32596528" target="_blank" style="text-decoration: none; color: #43443e;">Blog</a>
            </p>
            """,
            unsafe_allow_html=True)
        
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://github.com/ajstyle007/New-olympic-data-Analysis" target="_blank">
                    <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://github.com/ajstyle007/New-olympic-data-Analysis" target="_blank" style="text-decoration: none; color: #43443e;">Github</a>
            </p>
            """,
            unsafe_allow_html=True)

    # Content in the second column
    with col2:
        st.markdown(
            """
            ### Olympics Unveiled: An In-Depth Exploratory Data Analysis
            *I’ve developed a Streamlit web application to visualize and analyze Olympic data. 
            This app leverages interactive charts and plots to explore various metrics, such as athlete performance and medal distribution, 
            providing insights into trends and patterns across different Olympic events. 
            It enhances data understanding through user-friendly, real-time data exploration tools.*

            ***#Olympics #DataAnalysis #EDA #Visualizations #olympicsdataanalysis***
            """
        )

    st.markdown(
        """
        <hr style="border: none; height: 0.5px; background-color: #333;" />
        """,unsafe_allow_html=True)
    




# Blogs section
st.write("")
st.markdown("---")
st.write("")
st.markdown(
    """<div style="font-size: 35px; line-height: 1; margin-bottom: -10px; font-weight: bold; font-style: normal; font-family:Arial; color: #5a5f61;">
        Blogs
          </div>"""
          ,unsafe_allow_html=True,)

st.write("")
st.write("")


# Blog 0
st.markdown(
    """
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*fNLtC8C9-FGLl7meZsxUIA.png" alt="Blog Image" style="width: 100px; height: 100px; margin-right: 20px;">
        <div>
            <a href="https://medium.com/@kumarajaypaonta/behind-the-code-building-a-stock-market-chatbot-with-fastapi-selenium-and-langchain-b21e5dc88c6b" target="_blank" style="font-size: 18px; font-weight: bold; color: #5c5f56; text-decoration: none;">Behind the Code: Building a Stock Market Chatbot with FastAPI, Selenium and LangChain</a>
            <p style="font-size: 14px; color: #555;">Introduction, The stock market moves fast, 
            and so does the information around it. Traders often need to check multiple things at once — 
            best and worst performers of the day, single stock details, the latest news, sector trends, 
            or even a stock chart for a specific timeframe. Doing this manually can feel repetitive and 
            time-consuming. That’s where my project comes in.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# Blog 1
st.markdown(
    """
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*kr2AHoA-g8Rmd-dM4NePKA.png" alt="Blog Image" style="width: 100px; height: 100px; margin-right: 20px;">
        <div>
            <a href="https://medium.com/@kumarajaypaonta/linear-regression-101-everything-you-need-to-know-for-data-science-interviews-199034fcb7ee" target="_blank" style="font-size: 18px; font-weight: bold; color: #5c5f56; text-decoration: none;">Linear Regression 101: Everything You Need to Know for Data Science Interviews</a>
            <p style="font-size: 14px; color: #555;">Linear regression is one of the most fundamental algorithms in machine earning, widely used for 
            predictive modeling. In this guide, we’ll break down the key concepts, interview questions, and advanced techniques to help you master
              linear regression from the ground up.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Blog 2
st.markdown(
    """
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*QbxGwIoUxmyahVNNeyGG3Q.png" alt="Blog Image" style="width: 100px; height: 100px; margin-right: 20px;">
        <div>
            <a href="https://medium.com/@kumarajaypaonta/fighting-spam-with-machine-learning-building-an-effective-email-and-sms-classifier-96a5a201a954" target="_blank" style="font-size: 18px; font-weight: bold; color: #5c5f56; text-decoration: none;">Fighting Spam with Machine Learning: Building an Effective Email and SMS Classifier</a>
            <p style="font-size: 14px; color: #555;">Spam emails and SMS messages have become a significant concern in today’s digital world, 
            often cluttering inboxes with unwanted content or, worse, phishing attacks. These messages are an everyday nuisance, clogging our 
            inboxes with unsolicited or malicious content.
            Machine learning provides a powerful solution to automatically classify and filter these messages, improving the user experience.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Blog 3
st.markdown(
    """
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*_Ji2i4jYY827fXRRjswuwg.png" alt="Blog Image" style="width: 100px; height: 100px; margin-right: 20px;">
        <div>
            <a href="https://medium.com/@kumarajaypaonta/from-data-to-recommendations-creating-a-machine-learning-book-recommender-system-18fe5950368b" target="_blank" style="font-size: 18px; font-weight: bold; color: #5c5f56; text-decoration: none;">From Data to Recommendations: Creating a Machine Learning Book Recommender System</a>
            <p style="font-size: 14px; color: #555;">I implemented a popularity-based recommendation system for the Top 50 Books section. This system ranks books 
            based on overall popularity, considering factors like highest ratings, most reviews, and frequent user interactions. 
            It effectively showcases widely-loved and highly-rated books, making it ideal for users seeking to discover popular titles 
            that have already gained a strong reputation.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# import webbrowser
# if st.button("More Blogs"):
#     webbrowser.open("https://medium.com/me/stories/public")

st.markdown(
    """
    <a href="https://medium.com/me/stories/public" target="_blank">
        <button style="padding: 10px 20px; font-size: 16px; background-color: #43443e; color: #a4a79d; border: none; border-radius: 5px; cursor: pointer;">More Blogs</button>
    </a>
    """,
    unsafe_allow_html=True
)


# Blogs section
st.write("")
st.markdown("---")
st.write("")


st.markdown(
    """
    <style>
        .quote-container {
            border: 1px solid #ccc;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            background-color: #81857a;
        }

        .quote {
            font-family: "Times New Roman", Times, serif;
            font-size: 18px;
            margin-bottom: 10px;
            color: #d4dac9;
        }

        .author {
            font-style: italic;
            font-size: 14px;
            text-align: right;
            color: #464443;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
        """
        <div class="quote-container">
            <p class="quote">
                AI is going to bring a new renaissance for humanity, a new form of enlightenment, if you want, because AI is going to amplify everybody's intelligence.
            </p>
            <p class="author">- Yann LeCun</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.markdown("---")
st.write("")
st.markdown(
    """
    """
          ,unsafe_allow_html=True,)

st.write("")
st.write("")

# last part


st.markdown(
    """
    <div style="display: flex; justify-content: center; gap: 10px;">
        <span style="font-size: 15px; line-height: 1.5;">
            <a href="https://github.com/ajstyle007" target="_blank">
                <i class="fab fa-github" style="font-size: 25px; color: #464443;"></i>
            </a>
        </span>
        <span style="font-size: 15px; line-height: 1.5;">
            <a href="https://www.linkedin.com/in/ajay-kumar-72ba861b8/" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 25px; color: #464443;"></i>
            </a>
        </span>
        <span style="font-size: 15px; line-height: 1.5;">
            <a href="https://www.instagram.com" target="_blank">
                <i class="fab fa-instagram" style="font-size: 25px; color: #464443;"></i>
            </a>
        </span>
    </div>

    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <button style="background-color: #333; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; margin-right: 10px;">
            <a href="https://drive.google.com/file/d/1CV4KKP_bfnwi9CeTL7PEIIu8oOiAAs2Z/view?usp=sharing" download style="color: #fff; text-decoration: none;">Resume <i class="fas fa-download"></i></a>
        </button>
        <button style="background-color: #333; color: #fff; padding: 10px 20px; border: none; border-radius: 5px;">
            <a href="mailto:kumarajaypaonta@gmail.com" style="color: #fff; text-decoration: none;">Contact</a>
        </button>
    </div>

    </div>
    <div style="text-align: center; margin-top: 20px;">
        <p style="font-size: 12px; color: #464443;">&copy; 2025 Ajay Kumar. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
        html, body {
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        /* Keep Streamlit container padding intact to avoid hiding content */
        .main .block-container {
            padding-bottom: 10px !important; /* give bottom space for footer */
        }

        /* Footer wrapper that breaks out of container */
        .footer-wrapper {
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            width: 100vw;
            height: 150px;
            background-color: black;
            color:  white;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 7vw; /* big and responsive */
            font-weight: bold;
            font-family: 'Rajdhani', sans-serif;
            box-sizing: border-box;
            z-index: 9999;
            white-space: nowrap;
            overflow: hidden;
        }
    </style>

    <div class="footer-wrapper">
        प्रस्तुति – अजय
    </div>
""", unsafe_allow_html=True)


# st.markdown("""
#     <style>
#     .glow-text {
#         font-size: 48px;
#         font-weight: bold;
#         color: #fff;
#         text-align: center;
#         text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 30px #0ff, 0 0 30px #0ff;
#         margin-top: 50px;
#     }
#     </style>

#     <div class="glow-text"> Ajay का पोर्टफोलियो </div>
# """, unsafe_allow_html=True)



# st.markdown("""
#     <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap" rel="stylesheet">
#     <style>
#         html, body {
#             margin: 0;
#             padding: 0;
#             overflow-x: hidden;
#         }

#         .main .block-container {
#             padding-bottom: 10px !important;
#         }

#         .footer-wrapper {
#             left: 50%;
#             right: 50%;
#             margin-left: -50vw;
#             margin-right: -50vw;
#             width: 100vw;
#             max-width: 700px;
#             margin: 0 auto;
#             height: 200px;
#             background-color: #1f1f1f;
#             color: #add8e6;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             font-size: 3vw;
#             font-weight: 700;
#             font-family: 'Lobster', cursive;
#             font-size: 7vw;
#             border-radius: 200px;
#             box-shadow: 0 8px 20px rgba(0,0,0,0.3);
#             box-sizing: border-box;
#             z-index: 9999;
#         }
#     </style>

#     <div class="footer-wrapper">
#         Ajay Portfolio
#     </div>
# """, unsafe_allow_html=True)
