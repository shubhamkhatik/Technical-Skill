## Interview Questions Star component

### Solution 1

#### Star.js

```jsx
import React from "react";

const Star = ({ filled, half, onClick, onMouseMove }) => {
  // Decide which star to show
  let starChar = "☆";
  if (filled) starChar = "★";
  else if (half) starChar = "⯨"; // or use CSS for better visuals

  return (
    <span
      onClick={onClick}
      onMouseMove={onMouseMove}
      style={{
        cursor: "pointer",
        color: filled || half ? "#ffc107" : "#e4e5e9",
        fontSize: "32px",
        transition: "color 200ms",
        userSelect: "none",
      }}
    >
      {starChar}
    </span>
  );
};

export default Star;
```

#### StarRating.js

```jsx
import React, { useState } from "react";
import Star from "./Star";

const StarRatingWidget = ({ totalStars = 5 }) => {
  const [rating, setRating] = useState(0); // Selected rating
  const [hoverRating, setHoverRating] = useState(0); // Rating on hover

  const handleClick = (e, index) => {
    const isHalf = e.nativeEvent.offsetX < e.target.offsetWidth / 2;
    const newRating = index + (isHalf ? 0.5 : 1);
    setRating(newRating);
  };

  const getFillState = (index, ratingValue) => {
    if (index + 1 <= ratingValue) return { filled: true };
    if (index + 0.5 === ratingValue) return { half: true };
    return {};
  };

  return (
    <div style={{ display: "flex", gap: "8px" }}>
      {[...Array(totalStars)].map((_, index) => {
        const displayRating = hoverRating || rating;
        const { filled, half } = getFillState(index, displayRating);

        return (
          <Star
            key={index}
            filled={filled}
            half={half}
            onClick={(e) => handleClick(e, index)}
            onMouseMove={(e) => {
              const isHalf = e.nativeEvent.offsetX < e.target.offsetWidth / 2;
              setHoverRating(index + (isHalf ? 0.5 : 1));
            }}
            onMouseLeave={() => setHoverRating(0)}
          />
        );
      })}
    </div>
  );
};

export default StarRatingWidget;
```

### Solution 2

#### Star.js

```jsx
import React from "react";

const Star = ({
  filled,
  half,
  onClick,
  onMouseMove,
  onMouseLeave,
  onKeyDown,
  tabIndex,
}) => {
  return (
    <svg
      onClick={onClick}
      onMouseMove={onMouseMove}
      onMouseLeave={onMouseLeave}
      onKeyDown={onKeyDown}
      tabIndex={tabIndex}
      width="32"
      height="32"
      viewBox="0 0 24 24"
      style={{
        cursor: "pointer",
        color: filled || half ? "#ffc107" : "#e4e5e9",
        transition: "color 200ms",
        outline: "none",
      }}
      role="button"
      aria-label="Star rating"
    >
      {/* Full star path */}
      <path
        d="M12 .587l3.668 7.431L24 9.748l-6 5.854 1.417 8.265L12 19.771l-7.417 4.096L6 15.602 0 9.748l8.332-1.73z"
        fill={filled ? "#ffc107" : "#e4e5e9"}
      />
      {/* Half star overlay */}
      {half && (
        <path
          d="M12 .587l3.668 7.431L24 9.748l-6 5.854 1.417 8.265L12 19.771V.587z"
          fill="#ffc107"
        />
      )}
    </svg>
  );
};

export default Star;
```

#### StarRating.js

```jsx
import React, { useState } from "react";
import Star from "./Star";

const StarRatingWidget = ({ totalStars = 5 }) => {
  const [rating, setRating] = useState(0);
  const [hoverRating, setHoverRating] = useState(0);

  const getMouseFraction = (e) => {
    const { left, width } = e.currentTarget.getBoundingClientRect();
    const mouseX = e.clientX - left;
    return mouseX < width / 2 ? 0.5 : 1;
  };

  const handleClick = (e, index) => {
    const fraction = getMouseFraction(e);
    setRating(index + fraction);
  };

  const handleMouseMove = (e, index) => {
    const fraction = getMouseFraction(e);
    setHoverRating(index + fraction);
  };

  const handleKeyDown = (e) => {
    if (e.key === "ArrowRight") {
      setRating((prev) => Math.min(prev + 0.5, totalStars));
    }
    if (e.key === "ArrowLeft") {
      setRating((prev) => Math.max(prev - 0.5, 0));
    }
    if (e.key === "Enter") {
      setHoverRating(0); // lock in rating
    }
  };

  const getFillState = (index, value) => {
    if (index + 1 <= value) return { filled: true };
    if (index + 0.5 === value) return { half: true };
    return {};
  };

  const displayRating = hoverRating || rating;

  return (
    <div style={{ display: "flex", gap: "8px" }}>
      {[...Array(totalStars)].map((_, index) => {
        const { filled, half } = getFillState(index, displayRating);
        return (
          <Star
            key={index}
            filled={filled}
            half={half}
            onClick={(e) => handleClick(e, index)}
            onMouseMove={(e) => handleMouseMove(e, index)}
            onMouseLeave={() => setHoverRating(0)}
            onKeyDown={handleKeyDown}
            tabIndex={0}
          />
        );
      })}
    </div>
  );
};

export default StarRatingWidget;
```
