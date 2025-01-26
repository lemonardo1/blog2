
## 동적 자바스크립트 임베딩




%% DATAVIEW_PUBLISHER: start

```dataview
// DataviewJS 블록 내부에서 JavaScript 코드 사용 가능
let pages = dv.pages("#태그명")
  .where(p => p.file.name.includes("테스트"));  // 원하는 조건

for (let page of pages) {
  dv.el("p", `노트 이름: ${page.file.name}, 경로: ${page.file.path}`);
}

```
%%
%% DATAVIEW_PUBLISHER: end %%


## Iframe 임베딩 예시

아래는 Google Map을 iframe으로 임베딩한 예입니다:


<iframe
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.8354345094147!2d144.95373531531677!3d-37.81627977975159!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf5775555f3666e29!2sMelbourne%20City%20Center!5e0!3m2!1sen!2sau!4v1616237231056!5m2!1sen!2sau"
    width="600"
    height="450"
    style="border:0;"
    allowfullscreen=""
    loading="lazy"
></iframe>
