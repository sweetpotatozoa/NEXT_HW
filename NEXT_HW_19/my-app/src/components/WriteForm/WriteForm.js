import styles from './WriteForm.module.css';
import { useEffect, useState } from 'react';

const WriteForm = (props) => {
    const { addContent, updateContent, isEditing, editingContent } = props;
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    useEffect(() => {
        if (isEditing) {
            setTitle(editingContent.title);
            setContent(editingContent.content);
        }
    }, [isEditing, editingContent]);

    const submitHandler = (e) => {
        e.preventDefault();
        if (isEditing) {
            updateContent(editingContent.id, title, content);
        } else {
            addContent(title, content);
        }
        setTitle('');
        setContent('');
    };

    return (
        <div className={styles.write}>
            <input
                placeholder="제목을 입력하세요"
                className={styles.title}
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            ></input>
            <input
                placeholder="내용을 입력하세요"
                className={styles.content}
                value={content}
                onChange={(e) => setContent(e.target.value)}
            ></input>
            <button className={styles.button} onClick={(e) => submitHandler(e)}>
                {isEditing ? '수정하기' : '등록하기'}
            </button>
        </div>
    );
};
export default WriteForm;
