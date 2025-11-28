import streamlit as st

# Page config
st.set_page_config(page_title="Kloudstac - Cloud Solutions", page_icon="☁️", layout="wide")

# Custom CSS
st.markdown("""
<style>
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 4rem 2rem;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 3rem;
}
.hero-title {
    font-size: 4rem;
    font-weight: bold;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.hero-subtitle {
    font-size: 1.5rem;
    opacity: 0.9;
}
.card {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border: 1px solid #e0e0e0;
    height: 100%;
    transition: transform 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}
.icon-large {
    font-size: 3rem;
    margin-bottom: 1rem;
}
.advantage-item {
    display: flex;
    align-items: center;
    margin: 1rem 0;
    padding: 0.5rem;
    background: #f8f9fa;
    border-radius: 8px;
}
.advantage-icon {
    font-size: 1.5rem;
    margin-right: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-title">☁️ Welcome to Kloudstac</div>
    <div class="hero-subtitle">Empowering the Future of AI Integration</div>
</div>
""", unsafe_allow_html=True)

# Three column layout
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.markdown("""
    <div class="card">
        <h2 style="text-align: center; color: #1f77b4;">What is MCP?</h2>
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
        Model Context Protocol enables AI assistants to connect with external tools and data sources securely.
        </p>
        <div style="margin-top: 1.5rem;">
            <div class="advantage-item">
                <span class="advantage-icon">🔌</span>
                <div><strong>Universal Connectivity</strong><br>Connect to any data source or API</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">🛡️</span>
                <div><strong>Secure by Design</strong><br>Built-in authentication and authorization</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">🚀</span>
                <div><strong>High Performance</strong><br>Optimized for speed and efficiency</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">🔄</span>
                <div><strong>Real-time Updates</strong><br>Live data synchronization</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2 style="text-align: center; color: #1f77b4;">Use Cases</h2>
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
        Transform your business with powerful MCP integrations across industries.
        </p>
        <div style="margin-top: 1.5rem;">
            <div class="advantage-item">
                <span class="advantage-icon">💼</span>
                <div><strong>Enterprise Automation</strong><br>Streamline business processes</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">📊</span>
                <div><strong>Data Analytics</strong><br>Real-time insights and reporting</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">🛠️</span>
                <div><strong>DevOps Integration</strong><br>CI/CD pipeline automation</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">📱</span>
                <div><strong>Customer Support</strong><br>Intelligent helpdesk solutions</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h2 style="text-align: center; color: #1f77b4;">Why Choose MCP?</h2>
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
        Industry-leading protocol trusted by enterprises worldwide for AI integration.
        </p>
        <div style="margin-top: 1.5rem;">
            <div class="advantage-item">
                <span class="advantage-icon">⚙️</span>
                <div><strong>Easy Integration</strong><br>Simple setup and configuration</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">📈</span>
                <div><strong>Scalable Solution</strong><br>Grows with your business needs</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">🌐</span>
                <div><strong>Global Standards</strong><br>Compliant with international protocols</div>
            </div>
            <div class="advantage-item">
                <span class="advantage-icon">👥</span>
                <div><strong>Community Support</strong><br>Active developer ecosystem</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Call to action
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;">
    <h2>🌟 Ready to Transform Your AI Infrastructure?</h2>
    <p style="font-size: 1.2rem; margin-top: 1rem;">Experience the power of MCP integration today</p>
</div>
""", unsafe_allow_html=True)
