import React, { useState, useEffect, useRef } from 'react';
import './ChatBot.css';
import { useLanguage } from '../i18n/LanguageContext';

const ChatBot = ({ isOpen, onClose }) => {
  const { t } = useLanguage();
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (!sessionId) {
      setSessionId(generateSessionId());
    }
  }, [sessionId]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (isOpen && messages.length === 0) {
      setMessages([{
        type: 'bot',
        text: t('chat.welcomeMessage'),
        timestamp: new Date()
      }]);
    }
  }, [isOpen, messages.length, t]);

  const generateSessionId = () => {
    return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSend = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = {
      type: 'user',
      text: inputValue,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
          session_id: sessionId
        })
      });

      const data = await response.json();

      const botMessage = {
        type: 'bot',
        text: data.response,
        timestamp: new Date(),
        suggestedTours: data.suggested_tours || []
      };

      setMessages(prev => [...prev, botMessage]);
      setSessionId(data.session_id);
    } catch (error) {
      console.error('Ошибка отправки сообщения:', error);
      
      const errorMessage = {
        type: 'bot',
        text: t('chat.errorMessage'),
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const clearChat = () => {
    setMessages([{
      type: 'bot',
      text: t('chat.welcomeMessage'),
      timestamp: new Date()
    }]);
    setSessionId(generateSessionId());
  };

  if (!isOpen) return null;

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <h3>🤖 {t('chat.title')}</h3>
        <div className="chatbot-actions">
          <button onClick={clearChat} className="clear-btn" title={t('chat.clearTooltip')}>
            🔄
          </button>
          <button onClick={onClose} className="close-btn">
            ✕
          </button>
        </div>
      </div>

      <div className="chatbot-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.type}`}>
            <div className="message-content">
              <p>{message.text}</p>
              
              {message.suggestedTours && message.suggestedTours.length > 0 && (
                <div className="suggested-tours">
                  <h4>{t('chat.suggestedTours')}</h4>
                  {message.suggestedTours.map(tour => (
                    <div key={tour.id} className="mini-tour-card">
                      <h5>{tour.name}</h5>
                      <p>{tour.country}, {tour.city}</p>
                      <p><strong>{tour.duration_days} {t('tours.days')}</strong></p>
                      <p className="price">{parseFloat(tour.price).toLocaleString()} ₽</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
            <span className="message-time">
              {message.timestamp.toLocaleTimeString('ru-RU', { 
                hour: '2-digit', 
                minute: '2-digit' 
              })}
            </span>
          </div>
        ))}
        
        {isLoading && (
          <div className="message bot">
            <div className="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>

      <div className="chatbot-input">
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder={t('chat.placeholder')}
          rows="2"
          disabled={isLoading}
        />
        <button 
          onClick={handleSend} 
          disabled={!inputValue.trim() || isLoading}
          className="send-btn"
        >
          ➤
        </button>
      </div>
    </div>
  );
};

export default ChatBot;
