import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 页面配置
st.set_page_config(
    page_title="绿能巡洋 - AI数字邮轮系统",
    page_icon="🚢",
    layout="wide"
)

# 标题
st.title("🚢 绿能巡洋 - AI数字邮轮控制系统")
st.markdown("**智能·环保·安全** - 基于AI的下一代数字邮轮管理平台")

# 初始化会话状态
if 'current_scene' not in st.session_state:
    st.session_state.current_scene = "deepsea"
if 'passenger_count' not in st.session_state:
    st.session_state.passenger_count = 386

# 创建标签页
tab1, tab2, tab3 = st.tabs(["🏠 总览面板", "⚡ 能源管理", "🤖 AI助手"])

with tab1:
    st.header("智能场景控制")
    
    # 场景选择 - 使用唯一key
    scene = st.radio(
        "选择运行模式:",
        ["deepsea", "starry", "coral"],
        format_func=lambda x: {
            "deepsea": "🌊 深海模式", 
            "starry": "🌌 星空模式", 
            "coral": "🪸 珊瑚模式"
        }[x],
        key="scene_radio_main"
    )
    
    if scene != st.session_state.current_scene:
        st.session_state.current_scene = scene
        st.success(f"已切换到{scene}模式！")
    
    # 能源显示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("能源消耗", "1,250 kW", "-50 kW")
    with col2:
        efficiency = 0.85 if scene == "deepsea" else 0.65 if scene == "starry" else 0.75
        st.metric("能源效率", f"{efficiency*100:.1f}%")
    with col3:
        st.metric("在船乘客", f"{st.session_state.passenger_count}人")

with tab2:
    st.header("能源管理系统")
    
    # 能源分配滑块 - 使用唯一key
    energy_level = st.slider(
        "AI优化能源分配",
        0.5, 1.0, 0.75,
        help="AI将根据此设置自动调整设备运行",
        key="energy_slider_tab2"
    )
    
    st.info(f"当前能源分配: {energy_level*100:.1f}%")
    
    # 能源图表
    energy_data = pd.DataFrame({
        '时间': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00'],
        '能耗(kW)': [1200, 1250, 1180, 1320, 1270, 1240]
    })
    
    st.line_chart(energy_data.set_index('时间'))

with tab3:
    st.header("AI智能助手")
    
    # 初始化聊天历史
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # 显示聊天历史
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 聊天输入
    if prompt := st.chat_input("向AI助手提问关于邮轮运营的问题..."):
        # 添加用户消息
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # AI回复
        if "能源" in prompt.lower():
            response = "🔋 当前能源效率优秀，建议保持当前运行模式。"
        elif "乘客" in prompt.lower():
            response = f"👥 当前在船{st.session_state.passenger_count}人，服务系统运行正常。"
        elif "场景" in prompt.lower():
            response = f"🎮 当前运行{st.session_state.current_scene}模式，性能稳定。"
        else:
            response = "🤖 我是您的邮轮AI助手，可以帮您管理能源、监控系统状态。"
        
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # 重新运行以显示新消息
        st.rerun()

# 底部信息
st.markdown("---")
st.caption("绿能巡洋数字邮轮系统 © 2024 | 为可持续海洋生态而设计")