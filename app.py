import streamlit as st

#RAG - Inspired Knowledge Base
scheme_info={
    "Jal Jeevan Mission":"Provide safe drinking water to rural households.",
    
    "Samagra Siksha":"Supports quality education and school development.",
    
    "Ayushman Bharat":"Provides healthcare coverage for eligible families.",
    
    "Pradhan Mantri Gram Sadak Yojana":"Improves rural road connectivity.",
    
    "Skill India Mission":"Provides skill development and employment opportunities.",
    
    "Saubhagya Scheme":"Supports universal household electrification.",
    
    "Digital India":"Promotes digital infrastructure and connectivity.",
    
    "Swachh Bharat Mission":"Promotes sanitation and cleanliness initiative."
}

#Title
st.title("Village Insight AI")

#Description
st.write("AI-Powered Rural Problem Intelligence and Decision Support System")

#User Input
problem=st.text_area("Describe a Village Problem")

#Analyze Button
if st.button("Analyze Problem"):
    problem=problem.lower()
    
    #water Issue
    if "water" in problem:
        category="Water Supply"
        priority="High"
        scheme="Jal Jeevan Mission"
        sdg="SDG 6 - Clean Water And Sanitation"
        impact="High"
        confidence="95%"
        actions=["Repair damaged water pipelines",
                 "Promote rainwater harvesting",
                 "Conduct regular water quality testing"]
        
     
    #Education Issue    
    elif "school" in problem or "education" in problem:
        category="Education"
        priority="Medium"
        scheme="Samarga  Siksha"
        sdg="SDG 4 - Quality Education"
        impact="High"
        confidence="90%"
        actions=["Improve school infrastructure",
                 "Provide digital learning resources",
                 "Increase teacher availability"]
        
     
    #Healthcare Issue   
    elif "hospital" in problem or "health" in problem:
        category="Healthcare"
        priority="High"
        scheme="Ayushman Bharat"
        sdg="SDG 3 - Good Health And Well-being"
        impact="High"
        confidence="92%"
        actions=["Improve access to healthcare services",
                 "Organize health awareness camp",
                 "Strengthen primary healthcare facilities"]
        
    
    #Infrastructure Issue    
    elif "road" in problem:
        category="Infrastructure"
        priority="Medium"
        scheme="Pradhan Mantri Gram Sadak Yojana"
        sdg="SDG 11 - Sustainable Cities and Communities"
        impact="Medium"
        confidence="88%"
        actions=["Repair damaged roads",
                 "Improve transportation access",
                 "Increase infrastructure monitoring"]
        
        
    #Employment Issues
    elif "job" in problem or "employment" in problem or "unemployed" in problem or"unemployment" in problem or "work" in problem:
        category="Employment"
        priority="High"
        scheme="Skill India Mission"
        sdg="SDG 8 - Decent Work and Economic Growth"
        impact="High"
        confidence="89%"
        actions=["Organize skill development programs",
                 "Promote local entrepreneurship",
                 "Connect youth with employment schemes"]
        
        
    #Electricity Issues
    elif "electricity" in problem or "power" in problem or "light" in problem:
        category="Electricity Access"
        priority="High"
        scheme="Saubhagya Scheme"
        sdg="SDG 7 - Affordable and Clean Energy"
        impact="High"
        confidence="91%"
        actions=["Improve power distribution",
                 "Promote solar energy solutions",
                 "Monitor electricity outages"]
        
        
    #Internet Connectivity Issues
    elif "internet" in problem or "network" in problem or "connectivity" in problem:
        category="Digital Connectivity"
        priority="Medium"
        scheme="Digital India"
        sdg="SDG 9 - Industry, Innovation and Infrastructure"
        impact="High"
        confidence="87%"
        actions=["Expand broadband infrastructure",
                 "Improve mobile network coverage",
                 "Provide digital literacy programs"]
        
         
    #Sanitation Issues
    elif "toilet" in problem or "sanitation" in problem or "waste" in problem:
        category="Sanitation and Waste Management"
        priority="High"
        scheme="Swachh Bharat Mission"
        sdg="SDG 6 - Clean Water and Sanitation"
        impact="High"
        confidence="93%"
        actions=["Improve water collection systems",
                 "Promote sanitation awareness",
                 "Install proper waste disposal facilities"]
        
    
    #Default Case
    else:
        category="General Commiunity Issue"
        priority="Low"
        scheme="Further Assessement Required"
        sdg="SDG Assessment Needed"
        impact="Low"
        confidence="70%"
        actions=["Conduct detailed assessment",
                 "Gather additional community feedback",
                 "Consult local authorities"]
        
        
    #Result Section  
    st.subheader("Analysis Result")
    
    st.success(f"Category: {category}")
    
    st.warning(f"Priority Level: {priority}")
    
    st.info(f"Relevant Scheme: {scheme}")
    
    st.info(f"Related SDG: {sdg}")
    
    st.info(f"Sustainability Impact: {impact}")
    
    st.info(f"AI Confidence Score: {confidence}")
    
    #RAG-Inspired Retrieval
    if scheme in scheme_info:
        st.subheader("Scheme Information")
        st.write(scheme_info[scheme])
        
    #Recommend Actions
    st.subheader("Recommend Actions")
    
    for action in actions:
        st.write(f". {action}")
    
    #Divider
    st.divider()
    
    #AI Recommendation
    st.subheader("AI Generated Recommendation")
    
    
    st.write(f" This issue has been Calssified as {category}. "
             f" The priority level is {priority}. "
             f" The sustainability impact of resolving this issue is {impact}."
             f" The  AI system has identified {scheme} as the most relevant government support mechanism. "
             f" The recommend actions can improve well-being and contribute towards {sdg}."
             f" The model confidence for this assessment is {confidence}."
             )