const content = [
    { About: 'Custom SoftWare Development Company' },
    { Product: 'Web Development, Mobile Development, Desktop Development' },
    { Technology: '그런거 없어요' },
    { Downloads: '하지마요' },
];

const titleHandler = () => {
    const title = document.querySelector('.title');
    const navs = document.querySelectorAll('.nav');
    const subTitle = document.querySelector('.subTitle');

    navs.forEach((nav) => {
        nav.addEventListener('click', (e) => {
            title.innerText = e.target.innerText;
            content.forEach((k) => {
                if (Object.keys(k)[0] === e.target.innerText) {
                    subTitle.innerText = Object.values(k)[0];
                }
            });
        });
    });
};

titleHandler();
