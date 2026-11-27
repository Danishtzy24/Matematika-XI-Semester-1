export interface Detail { title: string; html: string; }
export interface PlayerStep { title: string; math: string; tip: string; why: string; }
export interface PlayerRow { title: string; math: string; colored: boolean; tip: string; why: string; }
export interface KnownItem { sym: string; val: string; }
export interface TopicPlayer { scene: string; vb: number[]; soal: string; given: KnownItem[]; goal: string; fRow: string; fColored: boolean; finish: string; finishPlain: string; rows: PlayerRow[]; }
export interface LessonSection { id: string; number: string; title: string; lead: string; details: Detail[]; search: string; player?: TopicPlayer; }
export interface Chapter { id: number; title: string; fullTitle: string; subtitle: string; intro: string; example: string; translation: string; sections: LessonSection[]; questions: string[]; }
export interface Option { id: string; html: string; text: string; }
export interface Question { id: string; chapter: number; prompt: string; options: Option[]; correct: string; correctSet?: string[]; text?: string; explanation: string; group: number; }
export interface Course { chapters: Chapter[]; questions: Question[]; summary: string; counts: {chapters: number; sections: number; questions: number}; }
export interface QuizSession { order: string[]; options: Record<string,string[]>; answers: Record<string,string>; submitted: boolean; }
export interface SavedState { version: number; current: number | 'mixed'; sessions: Record<string,QuizSession>; }
export interface SentenceToken { text: string; role: string; }
export interface VisualItem { label: string; parts: SentenceToken[]; formula: string; meaning: string; cue: string; }
export interface VisualModel { note: string; kind: string; items: VisualItem[]; timePosition?: number; }
