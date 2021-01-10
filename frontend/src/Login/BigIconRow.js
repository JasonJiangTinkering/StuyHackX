import React, { useRef, useEffect } from 'react';

const BigIconRow = ({topThree})=>{
  //   const parentRef   = useRef(null);
  //   const childrenRef = useRef(null);
  //   useEffect ( () => {
  //       // rerender 
  //     if(parentRef.current){
          
  //         let parentHeight = parentRef.current.offsetHeight;
  //         let parentWidth  = parentRef.current.offsetWidth;
          
  //     }
      
  //     if(childrenRef.current){
          
  //         let childrenHeight = childrenRef.current.offsetHeight;
  //         let childrenWidth  = childrenRef.current.offsetWidth;
          
  //     }
      
  // }, [parentRef, childrenRef]);
    return(
        <>
        <div id = "topStudents">
          <span id="left-Box" class ="bigThreeBoxs"></span>
          <span id="middle-Box" class ="bigThreeBoxs"></span>
          <span id="right-Box" class ="bigThreeBoxs"></span>

        </div>
        
        </>
    )
}

export default BigIconRow;