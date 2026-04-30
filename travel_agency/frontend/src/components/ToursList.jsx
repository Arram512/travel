import React from 'react';
import './ToursList.css';
import { useLanguage } from '../i18n/LanguageContext';

const ToursList = ({ tours }) => {
  const { t } = useLanguage();
  
  if (!tours || tours.length === 0) {
    return <div className="no-tours">{t('tours.noTours')}</div>;
  }

  const formatPrice = (price) => {
    return parseFloat(price).toLocaleString('ru-RU');
  };

  const getTourType = (tourType) => {
    return t(`tours.types.${tourType}`) || tourType;
  };

  return (
    <div className="tours-grid">
      {tours.map(tour => (
        <div key={tour.id} className="tour-card">
          <div className="tour-image">
            {tour.image_url ? (
              <img src={tour.image_url} alt={tour.name} />
            ) : (
              <div className="tour-image-placeholder">
                🌍
              </div>
            )}
            <div className="tour-badge">{getTourType(tour.tour_type)}</div>
          </div>
          
          <div className="tour-content">
            <h3>{tour.name}</h3>
            <p className="tour-location">📍 {tour.country}, {tour.city}</p>
            <p className="tour-description">{tour.description.substring(0, 150)}...</p>
            
            <div className="tour-details">
              <div className="tour-detail">
                <span className="icon">⏱</span>
                <span>{tour.duration_days} {t('tours.days')}</span>
              </div>
              <div className="tour-detail">
                <span className="icon">⭐</span>
                <span>{tour.rating}</span>
              </div>
            </div>
            
            <div className="tour-footer">
              <div className="tour-price">
                <span className="price-label">{t('tours.from')}</span>
                <span className="price-value">{formatPrice(tour.price)} ₽</span>
              </div>
              <button className="tour-btn">{t('tours.moreButton')}</button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ToursList;
