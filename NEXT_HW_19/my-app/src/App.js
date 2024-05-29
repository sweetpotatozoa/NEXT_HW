import './App.css';
import Header from './components/Header/Header';
import Word from './components/Word/Word';
import Title from './components/Title/Title';
import Content from './components/Content/Content';
import Write from './components/Write/Write';
import WriteForm from './components/WriteForm/WriteForm';
import { useState } from 'react';

function App() {
    const [isWriting, setIsWriting] = useState(0);
    const [contents, setContents] = useState([]);
    const [isEditing, setIsEditing] = useState(0);
    const [editingContent, setEditingContent] = useState({ id: 0, title: '', content: '' });

    const addContent = (title, content) => {
        const newContents = { id: contents.length + 1, title, content };
        setContents([...contents, newContents]);
        setIsWriting(0);
    };

    const deleteContent = (id) => {
        const newContents = contents.filter((content) => content.id !== id);
        setContents(newContents);
    };

    const updateContent = (id, title, content) => {
        const newContents = contents.map((a) => {
            if (a.id === id) {
                return { ...content, title, content };
            } else {
                return a;
            }
        });
        setContents(newContents);
        setIsEditing(0);
    };

    const editContent = (id, title, content) => {
        setEditingContent({ id, title, content });
        setIsEditing(1);
    };

    return (
        <>
            <Header title="상우의 시 노트"></Header>
            <Word word="자바칩이 되고파" word2="눈부신 일상 속에서 흑백의 휴식을 찾아서"></Word>
            <Title title="나의 글" poemNum="61편 씀"></Title>
            <Content contents={contents} deleteContent={deleteContent} editContent={editContent}></Content>
            {isWriting ? <WriteForm addContent={addContent}></WriteForm> : <Write setIsWriting={setIsWriting}></Write>}
            {isEditing && (
                <WriteForm
                    updateContent={updateContent}
                    isEditing={isEditing}
                    editingContent={editingContent}
                ></WriteForm>
            )}
        </>
    );
}

export default App;
