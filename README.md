# 1. 팀원 정보 및 업무 분담내역
## ⭐ 정현우(팀장)
- 컨셉 설정 및 계획 수립
- Navigator 이자 Driver

## ⭐ 김민균(팀원)
- 컨셉 설정 및 계획 수립
- Navigator 이자 Driver

### 현재까지 배웠던 내용을 총 복습 및 심화학습 할 수 있는 과정이기 때문에 Front와 back을 균등하게 접할 수 있도록 역할을 분배했다.

# 2. 목표 서비스 및 실제 구현 정도
## (1) User PlayList
<유저들이 자신만의 영화관을 만들다>
- 일반적인 음악 스트리밍 서비스에서 제공하는 "재생목록 "과 비슷한 기능을 생각했다. User들이 직접 제목을 붙혀 음악을 저장해 PlayList를 생성하는 것을 영화에 도입했다. User들이 자신만의 스타일로 PlayList를 만들어 다른 유저와 공유함으로써 다양한 타입의 영화를 접할 수 있는 MovieFlatForm을 제공하는 것이 우리 서비스의 핵심 과제이다.

## (2) 구현정도
- 처음 계획한 내용의 50%정도 구현했다고 생각한다. 50%는 기본 기능 구현, 나머지 50%가 PlayList라는 핵심기능 구현이었으나 기본기능 구현에서도 많은 시간을 쓰다보니 핵심기능을 구현하지 못했다.

# 3. 데이터베이스 모델링(ERD)

![리뷰](photo/ERD.png)

## (1) Moviedata_table
- 전체 영화 table
- 인기순 영화 table
- 평점 높은 순 영화 table
## (2) 기본 기능_table
- movie_review : 영화의 한줄평
- movie_like : 영화 좋아요
- review : 영화의 리뷰
- review_reviewcomment : 리뷰의 댓글
- user : 유정 정보 
- user_followers : 유저 팔로워, 팔로우
## (3) 추가 기능_table
- playlist : 각 유저의 플레이리스트
- playList_like : 각 플레이리스트의 좋아요

# 4. 영화 추천 알고리즘에 대한 기술적 설명
## (1) PlayList 알고리즘(실패)
- 유저들은 자신만의 PlayList파일을 만든다.
- 각자의 List를 공유할 수 있는 FlatForm에서 타유저의 List를 장문할 수 있다.
- 해당 유저가 가장 좋아하는 장르를 유저 정보로 입력 받고, 해당 장르를 가장 많이 포함하고 있는 플레이리스트를 추천해준다.
## (2) 장르별 알고리즘 추천
- PlayList기능을 구현하지 못했기 때문에 장르별 영화를 추천해 주는 기능으로 결정했디.

# 5.서비스 대표 기능에 대한 설명
## (1) 영화 추천 알고리즘
- swiper-slide 기능<br/>자동으로 영화의 포스터들이 전화이 되며 유저들이 편하게 볼 수 있게 해준다
![swiper](photo/swiper.png)

- 검색 기능 구현<br/> 입력하면 타이틀이나 장르에서 일치하는 해당 영화들을 전부 보여준다.
- 각 장르별로 버튼 구현<br/> 유저가 클릭하면 원하는 장르의 영화들을 소개해준다 
![swiper](photo/KakaoTalk_20230526_014356865_05.png)
- 영화 상세 페이지 구현<br/> 영화 포스터를 클릭하면 영화의 상세정보들이 모달로 나오는데 여기에는 영화의 예고편,&nbsp;포스터,&nbsp;제목&nbsp; 줄거리&nbsp; ... 등이 있고&nbsp;영화에 대한 한줄평 정도를 남길 수 있다.
![swiper](photo/KakaoTalk_20230526_014356865_06.png)
![swiper](photo/KakaoTalk_20230526_014356865_07.png)
![swiper](photo/KakaoTalk_20230526_014356865_08.png)
- 영화의 한줄평 기능(생성/삭제)<br/> 간단한 리뷰를 만들고 삭제한다 줄이 너무 길어질 경우 화면을 벗어나지 않도록 스크롤바를 만들어 유저들이 편리하게 이용할 수 있게 하였다. 
- Community에 Review (생성/수정/삭제)<br/> 자신이 좋아하는 영화를 다른 사람들에게 소개를 할 수 있는 공간을 만들었다
![swiper](photo/KakaoTalk_20230526_014356865_10.png)

# 6. 기타 (느낀 점, 후기 등)
사용자에게 편리하고 흥미로운 영화을 소개하기 위해 다양한 기능을 수현하고자 하였습니다. <br/><br/> 1. 영화를 데이터베이스와 연동하여 각 영화에 대한 상세한 정보를 제공하고 영화의 줄거리, 리뷰 및 평점 등을 통해 사용자에게 영화를 선택하는데 도움을 주고자 했습니다.<br/><br/>2. 영화 검색 기능 : 사용자가 원하는 영화를 쉽게 검색할 수 있는 기능을 제공하여 영화 제목, 장르 등을 활용하여 사용자는 빠르게 원하는 영화를 찾아볼 수 있습니다.<br/><br/>마지막 프로젝트를 하며 구현하지 못한 부분들에 대한 아쉬움이 남았지만 열심히해 후회는 없었습니다. <br/>디자인 부분에 부족함을 느꼈지만 사용자들에게 직관적이고 사용하기 쉽게 만들어 편리함에 매력을 느끼게 해주고 기능에 있어 영화를 소개해주기 뿐만 아니라 자신의 의견을 작성하며 사용자들간에 소통의 재미를 주고자 하였습니다. <br/>마지막으로 팀원과 소통을 하며 의견수많은 애러를 해결해 나아가며 많은 것을 배울 수 있는 좋은 프로젝트였다고 느꼈습니다.